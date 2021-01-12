from typing import Any

import pytest
from yummy_cereal import Serializer
from yummy_cereal import SerializerValidationFailed
from yummy_cereal import ValidatedSerializer


def test_ValidatedSerializer(value_serializer: Serializer[Any]) -> None:
    validators = [lambda x: x != 0, lambda x: x % 2 != 1]
    validated_serializer = ValidatedSerializer(lambda x: x, validators)

    with pytest.raises(SerializerValidationFailed):
        validated_serializer(0)

    with pytest.raises(SerializerValidationFailed):
        validated_serializer(1)

    assert validated_serializer(2) == 2
