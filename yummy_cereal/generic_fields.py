from typing import Any


def is_generic_list(cls: Any, attr_name: str) -> bool:
    """[summary]

    Args:
        obj (Any): [description]

    Returns:
        bool: [description]
    """
    return hasattr(cls, "__origin__") and cls.__origin__ == "List"


def is_generic_dict(cls: Any, attr_name: str) -> bool:
    """[summary]

    Args:
        obj (Any): [description]

    Returns:
        bool: [description]
    """
    return hasattr(cls, "__origin__") and cls.__origin__ == "Dict"
