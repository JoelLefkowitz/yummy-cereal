from typing import Any, Dict, TypeVar

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
