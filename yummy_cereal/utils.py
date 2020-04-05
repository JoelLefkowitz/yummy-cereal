from typing import Any, Dict, Tuple


def cls_is_annotated(cls: Any) -> bool:
    return hasattr(cls, "__dict__") and "__annotations__" in cls.__dict__


def cls_annotations(cls: Any) -> Dict:
    return cls.__dict__["__annotations__"].copy() if cls_is_annotated(cls) else {}


def is_proxy_dict(config: Any) -> bool:
    return isinstance(config, dict) and all(
        [
            isinstance(k, str) and (isinstance(v, dict) or isinstance(v, list))
            for k, v in config.items()
        ]
    )
