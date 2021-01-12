from yummy_cereal import AnnotationsParser

from ...models.people.house import House
from ...models.people.person import Person


def test_AnnotationsParser(big_bird: Person) -> None:
    house_parser = AnnotationsParser(House)
    person_parser = AnnotationsParser(Person, specified_parsers={House: house_parser})

    person = person_parser(
        {
            "name": big_bird.name,
            "house": {"number": big_bird.house.number, "street": big_bird.house.street},
        }
    )

    assert person == big_bird
