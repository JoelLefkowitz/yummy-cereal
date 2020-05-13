import pytest
from yummy_cereal import InvalidConfig, ValidatedParser


def test_AnotatedFieldsParser():
    pass


def test_ValidatedParser() -> None:
    parser = ValidatedParser(
        parser=int, validators=[lambda x: isinstance(x, str), lambda x: x.isdigit()]
    )
    assert parser("1") == 1
    assert parser("2") != 1

    with pytest.raises(InvalidConfig):
        parser(3)
