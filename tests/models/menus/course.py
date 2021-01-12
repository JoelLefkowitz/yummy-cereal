from dataclasses import dataclass
from dataclasses import field
from typing import List

from .dish import Dish


@dataclass
class Course:
    name: str
    dishes: List[Dish] = field(default_factory=list)
