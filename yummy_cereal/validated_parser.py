from dataclasses import dataclass
from typing import Callable, Dict, Generic, List, TypeVar

from .exceptions import InvalidConfig

T = TypeVar("T")
Validator = Callable[[Dict], bool]
Parser = Callable[[Dict], T]


@dataclass
class ValidatedParser(Generic[T]):
    parser: Parser[T]
    validators: List[Validator]

    def __call__(self, config: Dict) -> T:
        for validator in self.validators:
            if not validator(config):
                raise InvalidConfig({"Configuration": config, "Validator": validator})

        return self.parser(config)
