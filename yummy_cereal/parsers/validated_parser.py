from dataclasses import dataclass
from typing import Dict, Generic, List

from .. import Parser, Validator
from .exceptions import ValidationFailed


@dataclass
class ValidatedParser(Generic[T]):
    parser: Parser[T]
    validators: List[Validator]

    def __call__(self, config: Dict) -> T:
        for validator in self.validators:
            if not validator(config):
                raise ValidationFailed({"Configuration": config, "Validator": validator})

        return self.parser(config)
