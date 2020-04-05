from typing import Any


class InvalidConfig(Exception):
    def __init__(self, msg: str, config: Any) -> None:
        msg = f"Validation check failed\n{msg}\nConfig: {config}"
        super().__init__(msg)


class ConfigTypeError(Exception):
    def __init__(self, config: Any, expected_type: Any) -> None:
        msg = f"Config is not the expected type\nExpected: {expected_type}\nRecieved: {config}"
        super().__init__(msg)


class ConfigFormatError(Exception):
    def __init__(self, msg: str, config: Any) -> None:
        msg = (
            f"Config is not in the expected format\nExpected: {msg}\nRecieved: {config}"
        )
        super().__init__(msg)
