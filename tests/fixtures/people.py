import pytest

from ..models.people.house import House
from ..models.people.person import Person


@pytest.fixture
def sesame_street() -> House:
    return House(123, "Sesame Street")


@pytest.fixture
def big_bird(sesame_street: House) -> Person:
    return Person("Big Bird", sesame_street)
