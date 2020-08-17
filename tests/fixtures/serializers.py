from typing import Any, Dict

import pytest

from yummy_cereal import MissingFieldError


@pytest.fixture
def value_serializer(obj: Any) -> Dict:
    if not hasattr(config, "value"):
        raise MissingFieldError
    return config["value"]
