from typing import Any
from typing import Dict
from typing import TypeVar

from typing_inspect import get_args
from typing_inspect import get_origin

T = TypeVar("T")


def cls_is_annotated(cls: Any) -> bool:
    """
    Inspect if a class has annotations

    Args:  
        cls (Any): Class to inspect

    Returns:
        bool: True if cls is annotated else False
    """
    return (
        hasattr(cls, "__dict__")
        and "__annotations__" in cls.__dict__
        and len(cls.__dict__["__annotations__"]) > 0
    )


def get_cls_annotations(cls: Any) -> Dict:
    """
    Gets class annotations

    Args:
        cls (Any): Class to inspect

    Returns:
        Dict: Class annotations if cls is annotated else {}
    """
    if not cls_is_annotated(cls):
        return {}
    cls_annotations = cls.__dict__["__annotations__"].copy()  # type: Dict
    return cls_annotations


def field_is_generic_list(field: Any) -> bool:
    return get_origin(field) == list


def field_is_generic_dict(field: Any) -> bool:
    return get_origin(field) == dict


def get_primary_inner_type(field: Any) -> Any:
    return get_args(field)[0]


def is_named_class(cls: Any) -> bool:
    annotations = get_cls_annotations(cls)
    return len(annotations) == 2 and "name" in annotations
