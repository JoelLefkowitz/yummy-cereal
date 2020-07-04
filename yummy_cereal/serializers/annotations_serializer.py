from dataclasses import dataclass, field
from typing import Dict, Generic, TypeVar

from ..protocols import Factory, ParserMap

T = TypeVar("T")


@dataclass
class AnnotationsSerializer(Generic[T]):
    cls: Factory[T]
    field_defaults: Dict = field(default_factory=dict)
    specified_parsers: ParserMap = field(default_factory=dict)

    # TODO Write serializer method
    def __call__(self, obj: T) -> Dict:
        pass
