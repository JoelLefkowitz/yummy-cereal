from dataclasses import dataclass
from typing import Dict

from yummy_cereal.parsers.exceptions import MissingFieldError
from yummy_cereal.serializers.exceptions import MissingFieldError


@dataclass
class House:
    number: int
    street: str


def house_parser(config: Dict) -> House:
    if not "number" in config or not "street" in config:
        raise MissingFieldError()
    return House(config["number"], config["street"])


@dataclass
class House:
    number: int
    street: str
