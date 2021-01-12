from typing import Any

from yummy_cereal import OptionalParser
from yummy_cereal import Parser


def test_OptionalParser(value_parser: Parser[Any]) -> None:
    optional_parser = OptionalParser(value_parser)
    assert optional_parser({"value": 1}) == 1
    assert optional_parser(1) is None
