from typing import Any, Dict


def cls_is_annotated(cls: Any) -> bool:
    return hasattr(cls, "__dict__") and "__annotations__" in cls.__dict__


def cls_annotations(cls: Any) -> Dict:
    return cls.__dict__["__annotations__"].copy() if cls_is_annotated(cls) else {}
