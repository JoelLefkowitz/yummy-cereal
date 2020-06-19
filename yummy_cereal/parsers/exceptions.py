class ValidationFailed(Exception):
    msg = "The given object data failed a validation check"

    def __init__(self) -> None:
        super().__init__(self.msg)
