from dataclasses import dataclass
from typing import Dict, List

from yummy_cereal.generic_fields import is_generic_dict, is_generic_list


@dataclass
class AnnotatedClass:
    name: str
    names_list: List[str]
    names_dict: Dict[str, str]


def test_is_generic_list() -> None:
    assert is_generic_list(AnnotatedClass, "names_list")
    assert not is_generic_list(AnnotatedClass, "name")
    assert not is_generic_list(AnnotatedClass, "names_dict")


def test_is_generic_dict() -> None:
    assert is_generic_dict(AnnotatedClass, "names_dict")
    assert not is_generic_dict(AnnotatedClass, "name")
    assert not is_generic_dict(AnnotatedClass, "names_list")
