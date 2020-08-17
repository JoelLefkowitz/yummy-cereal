from dataclasses import dataclass
from typing import Dict, Generic, Optional, TypeVar

from ..protocols import Parser
from .exceptions import FieldParsingError

T = TypeVar("T")


@dataclass
class OptionalParser(Generic[T]):
    parser: Parser[T]

    def __call__(self, config: Dict) -> Optional[T]:
        try:
            return self.parser(config)
        except FieldParsingError:
            return None
