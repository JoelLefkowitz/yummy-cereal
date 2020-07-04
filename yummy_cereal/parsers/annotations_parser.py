from dataclasses import dataclass, field
from typing import Any, Dict, Generic, TypeVar

from typing_inspect import get_args

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
        parsed_fields = self.field_defaults.copy()
        parsed_fields.update({k: self.parse_field(k, v) for k, v in config.items()})
        return self.cls(**parsed_fields)

    def parse_field(self, field_name: Any, raw_field_value: Any) -> Any:
        annotations = get_cls_annotations(self.cls)
        field_type = annotations[field_name]

        if field_is_generic_list(self.cls, field_name):
            inner_field_type = get_args(field_type)[0]
            inner_field_parser = self.select_field_parser(inner_field_type)
            inner_field_annotations = get_cls_annotations(inner_field_type)

            if isinstance(raw_field_value, list):
                return [inner_field_parser(i) for i in raw_field_value]

            # TODO Tidy this up
            elif (
                isinstance(raw_field_value, dict)
                and "name" in inner_field_annotations
                and len(inner_field_annotations) == 2
            ):
                other_field = [i for i in inner_field_annotations if i != "name"].pop()
                return [
                    inner_field_parser({"name": k, other_field: v})
                    for k, v in raw_field_value.items()
                ]

            else:
                # TODO raise relevent exception
                raise Exception

        elif field_is_generic_dict(self.cls, field_name):
            inner_field_type = get_args(field_type)[0]
            inner_field_parser = self.select_field_parser(inner_field_type)
            inner_field_annotations = get_cls_annotations(inner_field_type)

            if isinstance(raw_field_value, dict):
                return {k: inner_field_parser(v) for k, v in raw_field_value.items()}

            else:
                # TODO raise relevent exception
                raise Exception

        else:
            field_parser = self.select_field_parser(field_type)

            if field_parser is Any:
                return raw_field_value

            else:
                return field_parser(raw_field_value)

    def select_field_parser(self, field_type: Any) -> Any:
        return (
            self.specified_parsers[field_type]
            if field_type in self.specified_parsers
            else field_type
        )
