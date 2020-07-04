from dataclasses import dataclass, field
from typing import Any, Dict, Generic, List, TypeVar

from typing_inspect import get_args

from ..exceptions import DictFieldParsingError, FieldParsingError, ListFieldParsingError
from ..protocols import Factory, ParserMap
from ..utils.annotations import (
    field_is_generic_dict,
    field_is_generic_list,
    get_cls_annotations,
)

T = TypeVar("T")


@dataclass
class AnnotationsParser(Generic[T]):
    cls: Factory[T]
    field_defaults: Dict = field(default_factory=dict)
    specified_parsers: ParserMap = field(default_factory=dict)

    def __call__(self, config: Dict) -> T:
        parsed_fields = {k: self.parse_field(k, v) for k, v in config.items()}
        parser_kwargs = {**self.field_defaults, **parsed_fields}
        return self.cls(**parser_kwargs)

    def select_field_parser(self, field_type: Any) -> Any:
        return (
            self.specified_parsers[field_type]
            if field_type in self.specified_parsers
            else field_type
        )

    def parse_field(self, field_name: Any, raw_field_value: Any) -> Any:
        annotations = get_cls_annotations(self.cls)
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
        if isinstance(raw_field_value, list):
            return [inner_field_parser(i) for i in raw_field_value]

        elif (
            isinstance(raw_field_value, dict)
            and len(inner_field_annotations) == 2
            and "name" in inner_field_annotations
        ):
            inner_field_annotations.pop("name")
            group_field, group_type = inner_field_annotations.popitem()
            return [
                inner_field_parser({"name": k, group_field: v})
                for k, v in raw_field_value.items()
            ]

        else:
            raise ListFieldParsingError(inner_field_parser, raw_field_value)

    def parse_dict_field(
        self,
        raw_field_value: Any,
        inner_field_parser: Any,
        inner_field_annotations: Dict,
    ) -> Dict:
        if isinstance(raw_field_value, dict):
            return {k: inner_field_parser(v) for k, v in raw_field_value.items()}

        else:
            raise DictFieldParsingError(inner_field_parser, raw_field_value)
