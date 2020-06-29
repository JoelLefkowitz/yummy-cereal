from dataclasses import dataclass, field
from typing import Any, Dict, Generic, TypeVar

from ..protocols import Factory, ParserMap
from ..utils.annotations import get_cls_annotations

T = TypeVar("T")


@dataclass
class AnnotationsParser(Generic[T]):
    cls: Factory[T]
    field_defaults: Dict = field(default_factory=dict)
    specified_parsers: ParserMap = field(default_factory=dict)

    def __call__(self, config: Dict) -> T:
        parsed_fields = self.field_defaults
        parsed_fields.update({k: self.parse_field(k, v) for k, v in config.items()})
        return self.cls(**parsed_fields)

    def parse_field(self, key: Any, value: Any) -> Any:
        annotations = get_cls_annotations(self.cls)
        field_type = annotations[key]
        field_parser = self.field_parsers[field_type]
        return field_parser(value)

    @property
    def field_parsers(self) -> ParserMap:
        annotations = get_cls_annotations(self.cls)
        parsers = {v: v for k, v in annotations.items()}
        parsers.update(self.specified_parsers)
        return parsers
