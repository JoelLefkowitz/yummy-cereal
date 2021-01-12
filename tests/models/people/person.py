from dataclasses import dataclass

from .house import House


@dataclass
class Person:
    name: str
    house: House
