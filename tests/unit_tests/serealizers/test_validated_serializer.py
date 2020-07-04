from dataclasses import dataclass
from typing import Dict

import pytest

from yummy_cereal import ValidatedSerializer, ValidationFailed


@dataclass
class Person:
    name: str


def person_serializer(person: Person) -> Dict:
    return {"name": person.name}


def test_ValidatedSerializer() -> None:
    name_validators = [lambda person: person.name != "Joel"]
    validated_serializer = ValidatedSerializer(person_serializer, name_validators)
    assert validated_serializer(Person("John")) == {"name": "John"}

    with pytest.raises(ValidationFailed):
        validated_serializer(Person("Joel"))
