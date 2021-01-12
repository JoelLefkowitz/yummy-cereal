# TODO serializer output format yaml or json

from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Dict
from typing import Generic
from typing import List
from typing import TypeVar

from typing_inspect import get_args

from ..protocols import Factory
from ..protocols import SerializerMap
from ..utils.annotations import field_is_generic_dict
from ..utils.annotations import field_is_generic_list
from ..utils.annotations import get_cls_annotations
from .exceptions import DictFieldSerializingError
from .exceptions import ListFieldSerializingError
from .exceptions import MissingFieldError

T = TypeVar("T")


@dataclass
class AnnotationsSerializer(Generic[T]):
    cls: Factory[T]
    field_defaults: Dict = field(default_factory=dict)
    specified_serializers: SerializerMap = field(default_factory=dict)

    def __call__(self, obj: T) -> Dict:
        """
        Serializes an object based on its class annotations

        Args:
            obj (T): Object to serialize

        Raises:
            MissingFieldError: An annotated was not provided a value

        Returns:
            Dict: Serialized object
        """
        annotations = get_cls_annotations(self.cls)
        serialized_fields = self.field_defaults.copy()

        for field_name, field_type in annotations.items():

            if field_is_generic_list(self.cls, field_name) and hasattr(obj, field_name):
                serialized_fields[field_name] = self.serialize_list_field(
                    obj, field_name, field_type
                )

            elif field_is_generic_dict(self.cls, field_name) and hasattr(
                obj, field_name
            ):
                serialized_fields[field_name] = self.serialize_dict_field(
                    obj, field_name, field_type
                )

            elif hasattr(obj, field_name):
                field_data = getattr(obj, field_name)
                field_serializer = self.select_field_serializer(field_type)

                serialized_fields[field_name] = (
                    field_data
                    if field_serializer is Any
                    else field_serializer(field_data)
                )

            elif field_name in self.field_defaults:
                serialized_fields[field_name] = self.field_defaults[field_name]

            else:
                raise MissingFieldError(obj, field_name)

        return serialized_fields

    def select_field_serializer(self, field_type: Any) -> Any:
        """
        Selects which serializer to use for a given field type

        Args:
            field_type (Any): Type of the field to serialize

        Returns:
            Any: Selected serializer to use
        """
        return (
            self.specified_serializers[field_type]
            if field_type in self.specified_serializers
            else field_type
        )

    def serialize_list_field(self, obj: Any, field_name: str, field_type: Any) -> List:
        """
        Serializes a list field with its inner type

        Args:
            obj (Any): Object to serialize
            field_name (str): Name of the object's list field
            field_type (Any): Type of the object's list field

        Raises:
            ListFieldSerializingError: The inner field data was not itself a list

        Returns:
            List: List of serialized inner objects
        """
        field_data = getattr(obj, field_name)
        inner_field_type = get_args(field_type)[0]
        inner_field_serializer = self.select_field_serializer(inner_field_type)

        if isinstance(field_data, list):
            return [inner_field_serializer(i) for i in field_data]

        else:
            raise ListFieldSerializingError(field_data, inner_field_serializer)

    def serialize_dict_field(self, obj: Any, field_name: str, field_type: Any) -> Dict:
        """
        Serializes a dict field with its inner type

        Args:
            obj (Any): Object to serialize
            field_name (str): Name of the object's dict field
            field_type (Any): Type of the object's dict field

        Raises:
            DictFieldSerializingError: The inner field data was not itself a dict

        Returns:
            Dict: Dict of serialized inner objects
        """
        field_data = getattr(obj, field_name)
        inner_field_type = get_args(field_type)[0]
        inner_field_serializer = self.select_field_serializer(inner_field_type)

        if isinstance(field_data, dict):
            return {k: inner_field_serializer(v) for k, v in field_data.items()}

        else:
            raise DictFieldSerializingError(
                field_data, inner_field_serializer,
            )
