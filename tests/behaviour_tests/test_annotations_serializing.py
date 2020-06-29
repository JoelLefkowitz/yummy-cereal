# coding=utf-8
"""Annotations serializing feature tests."""

from pytest_bdd import given, scenario, then, when


@scenario("annotations_serializing.feature", "Serializing a menu to a yaml file")
def test_serializing_a_menu_to_a_yaml_file():
    """Serializing a menu to a yaml file."""


@given("I have a menu object")
def i_have_a_menu_object():
    """I have a menu object."""


@given("I have annotated menu classes")
def i_have_annotated_menu_classes():
    """I have annotated menu classes."""


@when("I create a menu serializer")
def i_create_a_menu_serializer():
    """I create a menu serializer."""


@when("I serialize the menu object")
def i_serialize_the_menu_object():
    """I serialize the menu object."""


@then("I output the serialized menu")
def i_output_the_serialized_menu():
    """I output the serialized menu."""
