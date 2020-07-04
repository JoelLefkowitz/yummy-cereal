# coding=utf-8
"""Annotations parsing feature tests."""

import os
from typing import Dict

import pytest
from pytest_bdd import given, scenario, then, when

from yummy_cereal import AnnotationsParser
from yummy_cereal.utils.formatters import from_yaml

from ..fixtures.menus.classes import Course, Dish, Menu


@pytest.fixture()
def bdd_context() -> Dict:
    return {}


@scenario("annotations_parsing.feature", "Parsing a menu from a yaml file")
def test_parsing_a_menu_from_a_yaml_file():
    """Parsing a menu from a yaml file."""


@given("I have a serialized menu")
def i_have_a_serialized_menu(bdd_context: Dict):
    """I have a serialized menu."""
    bdd_context["serialized_menu"] = from_yaml(
        os.path.abspath("tests/fixtures/menus/menu.yml")
    )


@given("I have annotated menu classes")
def i_have_annotated_menu_classes():
    """I have annotated menu classes."""


@when("I create a menu parser")
def i_create_a_menu_parser(bdd_context: Dict):
    """I create a menu parser."""
    dish_parser = AnnotationsParser(Dish)
    course_parser = AnnotationsParser(Course, specified_parsers={Dish: dish_parser})
    bdd_context["menu_parser"] = AnnotationsParser(
        Menu, specified_parsers={Course: course_parser}
    )


@when("I parse the serialized menu")
def i_parse_the_serialized_menu(bdd_context: Dict):
    """I parse the serialized menu."""
    serialized_menu = bdd_context["serialized_menu"]
    menu_parser = bdd_context["menu_parser"]
    bdd_context["menu"] = menu_parser(serialized_menu)


@then("I recieve a menu object")
def i_recieve_a_menu_object(bdd_context: Dict):
    """I recieve a menu object."""
    menu = bdd_context["menu"]
    assert isinstance(menu, Menu)
    assert all([isinstance(course, Course) for course in menu.courses])
