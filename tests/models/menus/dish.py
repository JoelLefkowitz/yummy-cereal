from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import List


@dataclass
class Dish:
    name: str
    details: Any = None


@dataclass
class Course:
    name: str
    dishes: List[Dish] = field(default_factory=list)


@dataclass
class Menu:
    name: str
    languages: List[str]
    courses: List[Course] = field(default_factory=list)
    specials: List[Dish] = field(default_factory=list)
    drinks: List[Dish] = field(default_factory=list)
