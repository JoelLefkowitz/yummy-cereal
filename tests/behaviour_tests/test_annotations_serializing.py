# coding=utf-8
"""Annotations serializing feature tests."""

from typing import Dict

import pytest
from pytest_bdd import given, scenario, then, when

from yummy_cereal import AnnotationsSerializer

from ..fixtures.menus.classes import Course, Dish, Menu


@pytest.fixture()
def bdd_context() -> Dict:
    return {}


@scenario("annotations_serializing.feature", "Serializing a menu")
def test_serializing_a_menu():
    """Serializing a menu"""


@given("I have a menu object")
def i_have_a_menu_object(bdd_context: Dict):
    """I have a menu object."""
    bdd_context["menu"] = Menu(
        name="Big munch grill",
        languages=["English", "French"],
        courses=[
            Course("Appetizers", [Dish("Pico de Gallo"), Dish("Pineapple Salsa")])
        ],
        specials=[Dish("Banana split")],
    )


@given("I have annotated menu classes")
def i_have_annotated_menu_classes():
    """I have annotated menu classes."""


@when("I create a menu serializer")
def i_create_a_menu_serializer(bdd_context: Dict):
    """I create a menu serializer."""
    dish_serializer = AnnotationsSerializer(Dish)
    course_serializer = AnnotationsSerializer(
        Course, specified_serializers={Dish: dish_serializer}
    )
    bdd_context["menu_serializer"] = AnnotationsSerializer(
        Menu, specified_serializers={Course: course_serializer, Dish: dish_serializer}
    )


@when("I serialize the menu object")
def i_serialize_the_menu_object(bdd_context: Dict):
    """I serialize the menu object."""
    menu = bdd_context["menu"]
    menu_serializer = bdd_context["menu_serializer"]
    bdd_context["serialized_menu"] = menu_serializer(menu)


@then("I recieve a serialized menu")
def i_output_the_serialized_menu(bdd_context: Dict):
    """I recieve a serialized menu."""
    serialized_menu = bdd_context["serialized_menu"]
    assert isinstance(serialized_menu, Dict)
    print(serialized_menu)
    assert serialized_menu == {
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
        "locations": {},
    }
