from dataclasses import dataclass
from dataclasses import field
from typing import List

from .course import Course
from .dish import Dish


@dataclass
class Menu:
    name: str
    languages: List[str]
    courses: List[Course] = field(default_factory=list)
    specials: List[Dish] = field(default_factory=list)
    drinks: List[Dish] = field(default_factory=list)
