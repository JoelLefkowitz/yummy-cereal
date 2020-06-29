from dataclasses import dataclass
from typing import Dict

import pytest

from yummy_cereal import ValidatedParser, ValidationFailed


@dataclass
class Person:
    name: str


def person_parser(config: Dict) -> Person:
    return Person(config["name"])


def test_ValidatedParser() -> None:
    name_validators = [lambda config: config["name"] != "Joel"]
    validated_parser = ValidatedParser(person_parser, name_validators)
    assert validated_parser({"name": "John"}) == Person("John")

    with pytest.raises(ValidationFailed):
        validated_parser({"name": "Joel"})
