# coding=utf-8
"""Parser feature tests."""
import pytest
from pyimport import path_guard

path_guard("../..")

from pytest_bdd import given, scenario, then, when

from fixtures.menu_classes import Course, Dish, Menu
from yummy_cereal import AnotatedFieldsParser, list_or_single_parser, named_parser


@pytest.fixture(scope="module")
def context():
    return {}


@scenario("parsers.feature", "Parsing a menu")
def test_parsing_a_menu():
    """Parsing a menu."""


@given("I have annotated menu classes")
def annotated_menu_classes():
    """I have annotated menu classes."""
    pass


@when("I create menu parsers")
def create_menu_parser(context):
    """I create menu parsers."""
    dish_parser = AnotatedFieldsParser(
        cls=Dish, collector_field="details", child_parsers={"details": dict}
    )

    named_dish_list_parser = named_parser(list_or_single_parser(dish_parser))

    course_parser = AnotatedFieldsParser(
        cls=Course,
        collector_field="dishes",
        child_parsers={"dishes": named_dish_list_parser},
    )

    named_course_list_parser = named_parser(list_or_single_parser(course_parser))

    context["menu_parser"] = AnotatedFieldsParser(
        cls=Menu,
        collector_field="courses",
        child_parsers={"courses": named_course_list_parser},
    )


@when("I parse the menu")
def parse_menu(context, full_menu):
    """I parse the menu."""
    menu_parser = context["menu_parser"]
    context["menu"] = menu_parser(full_menu)


@then("I recieve menu objects")
def valid_menu_objs(context):
    """I recieve menu objects."""
    menu = context["menu"]
    assert ["Appetizers", "Mains", "Desserts", "Drinks", "Wines"] == [
        i.name for i in menu.courses
    ]

    main_course = next(course for course in menu.courses if course.name == "Mains")
    assert ["Pasta", "Pizza"] == [i.name for i in main_course.dishes]
