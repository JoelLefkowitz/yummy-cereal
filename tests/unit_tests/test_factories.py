from typing import Dict

import pytest
from pyimport import path_guard

path_guard("../..")

from fixtures.menu_classes import Menu, Course, Dish
from yummy_cereal import (
    InvalidConfig,
    ValidatedParser,
)

# AnotatedFieldsParser tested in behaviour_tests


def test_ValidatedParser() -> None:
    parser = ValidatedParser(
        parser=int, validators=[lambda x: isinstance(x, str), lambda x: x.isdigit()]
    )
    assert parser("1") == 1
    assert parser("2") != 1

    with pytest.raises(InvalidConfig):
        parser(3)
