from typing import Dict

import pytest
from pyimport import path_guard

path_guard("../..")

from fixtures.menu_classes import Course, Dish
from yummy_cereal import InvalidConfig, ValidatedParser, AnotatedFieldsParser


def test_ValidatedParser() -> None:
    parser = ValidatedParser(
        parser=int, validators=[lambda x: isinstance(x, str), lambda x: x.isdigit()]
    )
    assert parser("1") == 1
    assert parser("2") != 1

    with pytest.raises(InvalidConfig):
        parser(3)


def test_AnotatedFieldsParser(single_course_menu: Dict) -> None:
    parser = AnotatedFieldsParser(
        cls=Course, collector_field="dishes", child_parsers={"dishes": dict}
    )

    course = parser(single_course_menu)
    assert isinstance(course, Course)
    assert course.name == "Mains"

    # To decouple tests, no child parsers are used
    assert isinstance(course.dishes, dict)
