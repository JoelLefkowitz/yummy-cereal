from dataclasses import dataclass, field
from typing import Any, Dict, Generic, List, TypeVar

from typing_inspect import get_args

from ..protocols import Factory, ParserMap
from ..utils.annotations import (
    field_is_generic_dict,
    field_is_generic_list,
    get_cls_annotations,
)
from .exceptions import (
    DictFieldParsingError,
    FieldParsingError,
    ListFieldParsingError,
    MissingAnnotationError,
)

T = TypeVar("T")

# TODO Implement field_mappings
# TODO serializer output format yaml or json


@dataclass
class AnnotationsParser(Generic[T]):
    cls: Factory[T]
    field_defaults: Dict = field(default_factory=dict)
    field_mappings: Dict = field(default_factory=dict)
    specified_parsers: ParserMap = field(default_factory=dict)

    def __call__(self: T, config: Dict) -> T:
        """
        Parses an object based on its class annotations

        Args:
            config (Dict): Configuration to parse

        Returns:
            T: Parsed object
        """
        parsed_fields = {k: self.parse_field(k, v) for k, v in config.items()}
        parser_kwargs = {**self.field_defaults, **parsed_fields}
        return self.cls(**parser_kwargs)

    def select_field_parser(self, field_type: Any) -> Any:
        """
        Selects which parser to use for a given field type

        Args:
            field_type (Any): Type of the field to parse

        Returns:
            Any: Selected parser to use
        """
        return (
            self.specified_parsers[field_type]
            if field_type in self.specified_parsers
            else field_type
        )

    def parse_field(self, field_name: Any, raw_field_value: Any) -> Any:
        """
        Parses a field based on its class annotations

        Args:
            field_name (Any): Name of the object's field  
            raw_field_value (Any): Field data to parse 

        Raises:
            FieldParsingError: The field data could not be parsed

        Returns:
            Any: Parsed field data
        """

        #  TODO Check keys before lookup and raise exception
        annotations = get_cls_annotations(self.cls)

        if not field_name in annotations:
            raise MissingAnnotationError(field_name, annotations)

        field_type = annotations[field_name]

        if field_is_generic_list(self.cls, field_name):
            inner_field_type = get_args(field_type)[0]
            return self.parse_list_field(
                raw_field_value,
                self.select_field_parser(inner_field_type),
                get_cls_annotations(inner_field_type),
            )

        elif field_is_generic_dict(self.cls, field_name):
            inner_field_type = get_args(field_type)[0]
            return self.parse_dict_field(
                raw_field_value,
                self.select_field_parser(inner_field_type),
                get_cls_annotations(inner_field_type),
            )

        else:
            field_parser = self.select_field_parser(field_type)

            if field_parser is Any:
                return raw_field_value

            else:
                try:
                    return field_parser(raw_field_value)
                except TypeError:
                    raise FieldParsingError(field_parser, raw_field_value)

    def parse_list_field(
        self,
        raw_field_value: Any,
        inner_field_parser: Any,
        inner_field_annotations: Dict,
    ) -> List:
        """
        Parses an object's list field

        Args:
            raw_field_value (Any): List field data to parse
            inner_field_parser (Any): Inner field parser type
            inner_field_annotations (Dict): Annotations belonging to the inner field type

        Raises:
            ListFieldParsingError: The list field data was not itself or a list or able to be converted to a dictionary with names

        Returns:
            List: Parsed list field
        """

        if isinstance(raw_field_value, list):
            try:
                return [
                    inner_field_parser(i) if i is not None else None
                    for i in raw_field_value
                ]

            except TypeError:
                raise ListFieldParsingError(inner_field_parser, raw_field_value)

        elif (
            isinstance(raw_field_value, dict)
            and len(inner_field_annotations) == 2
            and "name" in inner_field_annotations
        ):
            inner_field_annotations.pop("name")
            group_field, group_type = inner_field_annotations.popitem()
            try:
                return [
                    inner_field_parser(
                        {"name": k, group_field: v if v is not None else None}
                    )
                    for k, v in raw_field_value.items()
                ]

            except TypeError:
                raise ListFieldParsingError(inner_field_parser, raw_field_value)

        else:
            raise ListFieldParsingError(inner_field_parser, raw_field_value)

    def parse_dict_field(
        self,
        raw_field_value: Any,
        inner_field_parser: Any,
        inner_field_annotations: Dict,
    ) -> Dict:
        """
        Parses an object's dict field

        Args:
            raw_field_value (Any): dict field data to parse
            inner_field_parser (Any): Inner field parser type
            inner_field_annotations (Dict): Annotations belonging to the inner field type

        Raises:
            DictFieldParsingError: The dict field data was not itself or a dict

        Returns:
            Dict: Parsed dict field
        """
        if not isinstance(raw_field_value, dict):
            raise DictFieldParsingError(inner_field_parser, raw_field_value)

        try:
            return {
                k: inner_field_parser(v) if v is not None else None
                for k, v in raw_field_value.items()
            }

        except TypeError:
            raise DictFieldParsingError(inner_field_parser, raw_field_value)
