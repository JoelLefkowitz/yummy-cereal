from dataclasses import dataclass

from yummy_cereal import AnnotationsParser


@dataclass
class House:
    number: int
    street: str


@dataclass
class Person:
    name: str
    house: House


def test_AnnotationsParser() -> None:
    person_parser = AnnotationsParser(Person)

    personal_details = {
        "name": "Joel",
        "house": {"number": 1, "street": "Sesame street"},
    }

    person = person_parser(personal_details)

    assert person.name == "Joel"
    assert person.house.number == 1
    assert person.house.street == "Sesame street"
