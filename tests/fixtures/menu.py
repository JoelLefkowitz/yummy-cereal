from typing import Dict

import pytest

from ..models.menus.course import Course
from ..models.menus.dish import Dish
from ..models.menus.menu import Menu


@pytest.fixture
def serialized_menu() -> Dict:
    return {
        "name": "Big munch grill",
        "languages": ["English", "French"],
        "courses": [
            {
                "name": "Appetizers",
                "dishes": [
                    {"name": "Pico de Gallo", "details": None},
                    {"name": "Pineapple Salsa", "details": None},
                ],
            }
        ],
        "specials": [{"name": "Banana split", "details": None}],
        "drinks": [],
    }


@pytest.fixture
def parsed_menu() -> Menu:
    return Menu(
        name="Big munch grill",
        languages=["English", "French"],
        courses=[
            Course("Appetizers", [Dish("Pico de Gallo"), Dish("Pineapple Salsa")])
        ],
        specials=[Dish("Banana split")],
    )
