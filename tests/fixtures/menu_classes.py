from dataclasses import dataclass
from typing import List


@dataclass
class Dish:
    name: str


@dataclass
class Course:
    name: str
    dishes: List[Dish]


@dataclass
class Menu:
    language: str
    courses: List[Course]
