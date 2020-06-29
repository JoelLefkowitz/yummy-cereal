from dataclasses import dataclass
from typing import Dict, List, TypeVar

from ..exceptions import ValidationFailed
from ..protocols import Serializer, Validator

T = TypeVar("T")


@dataclass
class ValidatedSerializer:
    serializer: Serializer[T]
    validators: List[Validator]

    def __call__(self, obj: T) -> Dict:
        for validator in self.validators:
            if not validator(obj):
                raise ValidationFailed(obj)
        return selfializer(obj)
