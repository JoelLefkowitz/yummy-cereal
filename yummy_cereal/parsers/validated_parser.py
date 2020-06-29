from dataclasses import dataclass
from typing import Dict, Generic, List, TypeVar

from ..exceptions import ValidationFailed
from ..protocols import Parser, Validator

T = TypeVar("T")


@dataclass
class ValidatedParser(Generic[T]):
    parser: Parser[T]
    validators: List[Validator]

    def __call__(self, config: Dict) -> T:
        for validator in self.validators:
            if not validator(config):
                raise ValidationFailed(config)
        return self.parser(config)
