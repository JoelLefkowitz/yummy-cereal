from typing import Dict, List

import pytest
from pyimport import path_guard

path_guard("../..")

from fixtures.menu_classes import Course, Dish
from yummy_cereal import (
    named_parser,
    list_parser,
    list_or_single_parser,
    ConfigFormatError,
    ConfigTypeError,
)


def dish_parser(data: Dict) -> Dish:
    return Dish(**data)


def test_named_parser(single_dish_menu: Dict) -> None:
    parser = named_parser(dish_parser)
    dish = parser(single_dish_menu)
    assert dish.name == "Pasta"


def test_list_parser(simple_dishes_menu: List) -> None:
    parser = list_parser(dish_parser)
    dish_lst = parser(simple_dishes_menu)

    print(dish_lst)

    assert isinstance(dish_lst, list)
    assert all(isinstance(dish, Dish) for dish in dish_lst)
    assert dish_lst[0].name == "Pasta"
    assert dish_lst[1].name == "Pizza"


def test_list_or_single_parser(
    simple_dishes_menu: List, simple_single_dish_menu: Dict
) -> None:
    parser = list_or_single_parser(dish_parser)
    dish_lst = parser(simple_dishes_menu)

    assert isinstance(dish_lst, list)
    assert all(isinstance(dish, Dish) for dish in dish_lst)
    assert dish_lst[0].name == "Pasta"
    assert dish_lst[1].name == "Pizza"

    single_dish = parser(simple_single_dish_menu)
    assert isinstance(single_dish, Dish)
    assert single_dish.name == "Pasta"
