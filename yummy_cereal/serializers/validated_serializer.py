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
        """
        Runs each of self.validatiors the calls self.serializer on success

        Args:
            obj (T): Object to be serialized

        Raises:
            ValidationFailed: One or more validators will return False

        Returns:
            Dict: Serialized object
        """        
        for validator in self.validators:
            if not validator(obj):
                raise ValidationFailed(obj)
        return self.serializer(obj)
