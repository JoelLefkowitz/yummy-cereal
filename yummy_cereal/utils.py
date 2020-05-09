from typing import Any, Dict


def cls_is_annotated(cls: Any) -> bool:
    return hasattr(cls, "__dict__") and "__annotations__" in cls.__dict__


def cls_annotations(cls: Any) -> Dict:
    return cls.__dict__["__annotations__"].copy() if cls_is_annotated(cls) else {}


def is_generic_list(obj: Any) -> bool:
    return hasattr(obj, "__origin__") and obj.__origin__ == list


def is_generic_dict(obj: Any) -> bool:
    return hasattr(obj, "__origin__") and obj.__origin__ == "Dict"


def inner_type(generic_field_type: Any) -> bool:
    return generic_field_type.__args__[0]
