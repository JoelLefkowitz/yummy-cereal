from typing import Any


class ValidationFailed(Exception):
    def __init__(self, obj: Any) -> None:
        msg = f"The given object data failed a validation check\n{obj}"
        super().__init__(msg)
