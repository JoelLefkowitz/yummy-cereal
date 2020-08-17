from typing import Any

import pytest

from yummy_cereal import Parser, ParserValidationFailed, ValidatedParser


def test_ValidatedParser(value_parser: Parser[Any]) -> None:
    validators = [lambda x: x != 0, lambda x: x % 2 != 1]
    validated_parser = ValidatedParser(value_parser, validators)

    with pytest.raises(ParserValidationFailed):
        validated_parser({"value": 0})

    with pytest.raises(ParserValidationFailed):
        validated_parser({"value": 1})

    assert validated_parser({"value": 2}) == 2
