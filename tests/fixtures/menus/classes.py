from dataclasses import dataclass
from typing import Any, List


@dataclass
class Dish:
    name: str
    details: Any = None


@dataclass
class Course:
    name: str
    dishes: List[Dish]


@dataclass
class Menu:
    name: str
    language: str
    courses: List[Course]
    specials: List[Dish]
    drinks: List[Dish]
