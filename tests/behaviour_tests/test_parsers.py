# coding=utf-8
"""Parser feature tests."""

from pyimport import path_guard

path_guard("../..")

from pytest_bdd import given, scenario, then, when

from fixtures.menu_classes import Course, Dish, Menu
from yummy_cereal import annotations_parser_factory, list_or_single_parser, named_parser


@scenario("features/parsers.feature", "Parsing a menu")
def test_parsing_a_menu():
    """Parsing a menu."""


@given("I have annotated menu classes")
def i_have_annotated_menu_classes():
    """I have annotated menu classes."""
    pass


@when("I create menu parsers")
def i_create_menu_parsers():
    """I create menu parsers."""
    pass


@when("I parse the menu")
def i_parse_the_menu():
    """I parse the menu."""
    pass


@then("I recieve menu objects")
def i_recieve_menu_objects():
    """I recieve menu objects."""
    pass
