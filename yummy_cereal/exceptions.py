class PrettyException(Exception):
    msg: str

    def __init__(self, *args, **kwargs) -> None:
        runtime = [f"{x}" for x in args] + [f"{k}: {v}" for k, v in kwargs.items()]
        error_message = self.msg + "Runtime context:" + "\n".join(runtime)
        super().__init__(error_message)


class InvalidConfig(PrettyException):
    msg = "The given configuration failed a validation check"


class ConfigTypeError(PrettyException):
    msg = "Cannot parse the given configuration. Expected a dictionary type"


class AnnotationTypeError(PrettyException):
    msg = "Annotated field type could not parse the given configuration"
