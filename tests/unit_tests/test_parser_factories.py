from typing import Dict
import pytest
from pyimport import path_guard

path_guard("../..")
from yummy_cereal import ValidatedParser, annotations_parser_factory, InvalidConfig
from fixtures.menu_classes import Dish, Course


def test_ValidatedParser() -> None:
    parser = ValidatedParser(
        parser=int, validators=[lambda x: isinstance(x, str), lambda x: x.isdigit()]
    )
    assert parser("1") == 1
    assert parser("2") != 1

    with pytest.rasies(InvalidConfig):
        parser(3)


def test_annotations_parser_factory(single_course_menu: Dict) -> None:
    parser = annotations_parser_factory(
        cls=Course,
        omit_fields=None,
        collector_field="dishes",
        child_parsers={"Dish": Dish},
    )

    parser(single_course_menu)
