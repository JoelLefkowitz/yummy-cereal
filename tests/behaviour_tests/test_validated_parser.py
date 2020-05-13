import pytest
from fixtures.menus.models import Course, Dish, Menu
from pytest_bdd import given, scenario, then, when
from yummy_cereal import AnotatedFieldsParser, InvalidConfig, ValidatedParser


@pytest.fixture(scope="module")
def context():
    return {}


@scenario("validated_parser.feature", "Validating a menu")
def test_validating_a_menu():
    """Validating a menu."""


@given("I have a menu parser")
def menu_parser(context):
    """I have a menu parser."""
    dish_parser = AnotatedFieldsParser(cls=Dish, collector_field="details")

    course_parser = AnotatedFieldsParser(
        cls=Course,
        collector_field="dishes",
        collect_with_names=True,
        typed_parsers={Dish: dish_parser},
    )

    menu_parser = AnotatedFieldsParser(
        cls=Menu,
        collector_field="courses",
        collect_with_names=True,
        typed_parsers={Course: course_parser},
    )

    context["menu_parser"] = menu_parser


@given("I create a validated parser")
def validated_parser(context):
    """I create a validated parser."""
    validators = [
        lambda x: ("courses" in x and "Mains" in x["courses"], "Mains not in menu")
    ]
    validated_parser = ValidatedParser(context["menu_parser"], validators)
    context["validated_parser"] = validated_parser


@when("I parse and validate a menu")
def validate_menu(context, full_menu, invalid_menu):
    """I parse and validate a menu."""
    menu_parser = context["validated_parser"]

    # Validation checks are run when parsing
    menu_parser(full_menu)

    with pytest.raises(InvalidConfig):
        menu_parser(invalid_menu)


# Validation checks run during menu parsing
@then("Validation checks are run")
def validate_objs(context):
    """Validation checks are run."""
