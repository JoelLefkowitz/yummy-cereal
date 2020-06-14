from dataclasses import dataclass
from typing import TypeVar, Dict

import pytest

from yummy_cereal import InvalidConfig, ValidatedParser

T = TypeVar("T")


@dataclass
class Person:
    name: str

    @classmethod
    def from_dict(cls: T, config: Dict) -> T:
        return cls(config["name"])


def test_ValidatedParser() -> None:
    person_parser = Person.from_dict
    name_validators = [lambda config: config["name"] != "Joel"]

    validated_parser = ValidatedParser(person_parser, name_validators)
    assert validated_parser({"name": "John"}) == Person("John")

    with pytest.raises(InvalidConfig):
        validated_parser({"name": "Joel"})
