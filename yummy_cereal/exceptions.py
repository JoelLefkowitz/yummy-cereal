from typing import Dict


class PrettyException(Exception):
    msg: str

    def format_error_message(self, **kwargs) -> str:
        return self.msg + "\n".join(**kwargs.items())


class InvalidConfig(PrettyException):
    msg = "The given configuration failed a validation check"

    def __init__(self, config: Dict) -> None:
        super().__init__(self.format_error_message(config))


class ConfigTypeError(PrettyException):
    msg = "Cannot parse the given configuration. Expected a dictionary type"

    def __init__(self, runtime_kwargs: Dict) -> None:
        super().__init__(self.msg + runtime)


class AnnotationTypeError(PrettyException):
    msg = "Annotated field type could not parse the given configuration"

    def __init__(self, runtime_kwargs: Dict) -> None:
        super().__init__(self.msg + runtime)
