from typing import Any


class InvalidConfig(Exception):
    def __init__(self, msg: str, config: Any) -> None:
        msg = f"Validation check failed\n{msg}\nConfig: {config}"
        super().__init__(msg)


class ConfigTypeError(Exception):
    def __init__(self, config: Any) -> None:
        msg = (
            f"Config is not a dictionary type\nExpected: Dictionary\nRecieved: {config}"
        )
        super().__init__(msg)


class AnnotationTypeError(Exception):
    def __init__(self, annotation_type: Any, config: Any) -> None:
        msg = f"Annotated field type failed to parse config\nType: {annotation_type}\nConfig: {config}"
        super().__init__(msg)
