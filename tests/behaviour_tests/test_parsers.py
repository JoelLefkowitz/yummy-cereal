# import pytest
# from pytest_bdd import given, scenario, then, when

# from fixtures.menu import Course, Dish, Menu
# from yummy_cereal import AnotatedFieldsParser


# @pytest.fixture(scope="module")
# def context():
#     return {}


# @scenario("parsers.feature", "Parsing a menu")
# def test_parsing_a_menu():
#     """Parsing a menu."""


# @given("I have annotated menu classes")
# def annotated_menu_classes():
#     """I have annotated menu classes."""


# @when("I create a menu parser")
# def create_menu_parser(context):
#     """I create a menu parser."""
#     dish_parser = AnotatedFieldsParser(cls=Dish, collector_field="details")

#     course_parser = AnotatedFieldsParser(
#         cls=Course,
#         collector_field="dishes",
#         collect_with_names=True,
#         typed_parsers={Dish: dish_parser},
#     )

#     menu_parser = AnotatedFieldsParser(
#         cls=Menu, collect_with_names=True, typed_parsers={Course: course_parser},
#     )

#     context["menu_parser"] = menu_parser


# @when("I parse a menu")
# def parse_menu(context, full_menu):
#     """I parse a menu."""
#     menu_parser = context["menu_parser"]
#     context["menu"] = menu_parser(full_menu)


# @then("The menu data is validated")
# def validate_menu_data(context):
#     pass


# @then("I recieve menu objects")
# def valid_menu_objs(context):
#     """I recieve menu objects."""
#     menu = context["menu"]
#     assert menu.language == "English"

#     course_names = [course.name for course in menu.courses]
#     assert course_names == [
#         "Appetizers",
#         "Mains",
#         "Desserts",
#         "Drinks",
#         "Wines",
#     ]

#     mains = menu.courses[course_names.index("Mains")]
#     assert [dish.name for dish in mains.dishes] == ["Pasta", "Pizza"]