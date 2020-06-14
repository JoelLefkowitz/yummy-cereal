from dataclasses import dataclass

from yummy_cereal import AnnotationsParser


@dataclass
class House:
    number: int
    street: str


def test_AnnotationsParser() -> None:
    house_parser = AnnotationsParser(cls=House)
    house = house_parser({"number": 1, "street": "Sesame street"})
    assert house.number == 1
    assert house.street == "Sesame street"
