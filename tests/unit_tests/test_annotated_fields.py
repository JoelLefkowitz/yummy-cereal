from dataclasses import dataclass
from typing import Dict, List

from yummy_cereal.annotated_fields import (
    cls_is_annotated,
    field_is_generic_dict,
    field_is_generic_list,
    get_cls_annotations,
)


@dataclass
class AnnotatedClass:
    name: str
    names_list: List[str]
    names_dict: Dict[str, str]


class BlankClass:
    pass


def test_cls_is_annotated() -> None:
    assert cls_is_annotated(AnnotatedClass)
    assert not cls_is_annotated(BlankClass)


def test_get_cls_annotations() -> None:
    assert get_cls_annotations(AnnotatedClass) == {
        "name": str,
        "names_list": List[str],
        "names_dict": Dict[str, str],
    }
    assert get_cls_annotations(BlankClass) == {}


def test_is_generic_list() -> None:
    assert field_is_generic_list(AnnotatedClass, "names_list")
    assert not field_is_generic_list(AnnotatedClass, "name")
    assert not field_is_generic_list(AnnotatedClass, "names_dict")


def test_is_generic_dict() -> None:
    assert field_is_generic_dict(AnnotatedClass, "names_dict")
    assert not field_is_generic_dict(AnnotatedClass, "name")
    assert not field_is_generic_dict(AnnotatedClass, "names_list")
