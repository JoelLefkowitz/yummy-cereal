from dataclasses import dataclass
from typing import Dict
from typing import Generic
from typing import Optional
from typing import TypeVar

from ...protocols import Parser
from ..exceptions import ParsingError

T = TypeVar("T")


@dataclass
class OptionalParser(Generic[T]):
    parser: Parser[T]

    def __call__(self, config: Dict) -> Optional[T]:
        try:
            return self.parser(config)
        except ParsingError:
            return None
