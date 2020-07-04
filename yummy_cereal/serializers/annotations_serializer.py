from dataclasses import dataclass, field
from typing import Any, Dict, Generic, TypeVar, List, Dict

from ..exceptions import MissingFieldError
from ..protocols import Factory, SerializerMap
from ..utils.annotations import get_cls_annotations, field_is_generic_list, field_is_generic_dict

T = TypeVar("T")


@dataclass
class AnnotationsSerializer(Generic[T]):
    cls: Factory[T]
    field_defaults: Dict = field(default_factory=dict)
    specified_serializers: SerializerMap = field(default_factory=dict)

    def __call__(self, obj: T) -> Dict:
        annotations = get_cls_annotations(self.cls)
        serialized_fields = self.field_defaults.copy()

        for field_name, field_type in annotations.items():

            if field_is_generic_list(self.cls, field_name):
                serialized_fields[field_name] = self.serialize_list_field(obj, field_name)

            elif field_is_generic_dict(self.cls, field_name):
                serialized_fields[field_name] = self.serialize_dict_field(obj, field_name)

            elif hasattr(obj, field_name):
                field_data = getattr(obj, field_name)
                field_serializer = self.select_field_serializer(field_type)
                serialized_fields[field_name] = field_serializer(field_data)

            elif field_name in self.field_defaults:
                serialized_fields[field_name] = self.field_defaults[field_name]

            else:
                raise MissingFieldError(obj, field_name)

        return serialized_fields

    def select_field_serializer(self, field_type: Any) -> Any:
        return (
            self.specified_serializers[field_type]
            if field_type in self.specified_serializers
            else field_type
        )

    # TODO Write method
    def serialize_list_field(self, obj: Any, field_name: str) -> List:
        return []

    # TODO Write method
    def serialize_dict_field(self, obj: Any, field_name: str) -> Dict:
        return {}