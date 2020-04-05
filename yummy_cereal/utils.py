from typing import Any, Dict, Tuple


def cls_is_annotated(cls: Any) -> bool:
    return hasattr(cls, "__dict__") and "__annotations__" in cls.__dict__


def cls_annotations(cls: Any) -> Dict:
    return cls.__dict__["__annotations__"].copy() if cls_is_annotated(cls) else {}


def first_items(config: Dict) -> Tuple:
    return list(config.items())[0]


def is_proxy_dict(config: Any) -> bool:
    return all(
        [
            isinstance(config, dict),
            len(config) == 1,
            isinstance(first_items(config)[0], str),
            isinstance(first_items(config)[1], dict),
        ]
    )
