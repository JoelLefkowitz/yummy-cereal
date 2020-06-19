from typing import Any, Dict, TypeVar

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


def field_is_generic_list(cls: Any, attr_name: str) -> bool:
    """
    Inspects if a class's attribute is a generic list

    Args:
        cls (Any): Class to inspect 

    Returns:
        bool: True if attribute is a generic list
    """
    annotations = get_cls_annotations(cls)
    return attr_name in annotations and get_origin(annotations[attr_name]) == list


def field_is_generic_dict(cls: Any, attr_name: str) -> bool:
    """
    Inspects if a class's attribute is a generic dict

    Args:
        cls (Any): Class to inspect 

    Returns:
        bool: True if attribute is a generic dict
    """
    annotations = get_cls_annotations(cls)
    return attr_name in annotations and get_origin(annotations[attr_name]) == dict
