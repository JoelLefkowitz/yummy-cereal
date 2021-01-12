from yummy_cereal import AnnotationsSerializer

from ...models.people.house import House
from ...models.people.person import Person


def test_AnnotationsSerializer(big_bird: Person) -> None:
    house_serializer = AnnotationsSerializer(House)
    person_serializer = AnnotationsSerializer(
        Person, specified_serializers={House: house_serializer}
    )

    serialized_person = person_serializer(big_bird)
    assert serialized_person["name"] == big_bird.name
    assert serialized_person["house"]["number"] == big_bird.house.number
    assert serialized_person["house"]["street"] == big_bird.house.street
