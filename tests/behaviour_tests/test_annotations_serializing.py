# coding=utf-8
"""Annotations serializing feature tests."""

from typing import Dict

import pytest
from pytest_bdd import given, scenario, then, when

from yummy_cereal import AnnotationsSerializer

from ..models.menus.course import Course
from ..models.menus.dish import Dish
from ..models.menus.menu import Menu


@pytest.fixture()
def bdd_context() -> Dict:
    return {}


@scenario("annotations_serializing.feature", "Serializing a menu")
def test_serializing_a_menu():
    """Serializing a menu"""


@given("I have a menu object")
def i_have_a_menu_object():
    """I have a menu object."""


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
def i_serialize_the_menu_object(bdd_context: Dict, parsed_menu: Menu):
    """I serialize the menu object."""
    menu_serializer = bdd_context["menu_serializer"]
    bdd_context["serialized_menu"] = menu_serializer(parsed_menu)


@then("I recieve a serialized menu")
def i_output_the_serialized_menu(bdd_context: Dict, serialized_menu: Dict):
    """I recieve a serialized menu."""
    assert bdd_context["serialized_menu"] == serialized_menu
