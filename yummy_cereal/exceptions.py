class InvalidStructure(Exception):
    def __init__(self, config) -> None:
        msg = f"The config '{config}' cannot be parsed by a parser"
        super().__init__(msg)


class UnparsedConfig(Exception):
    def __init__(self, config) -> None:
        msg = f"The config '{config}' did not get parsed by a child parser or match any named attributes"
        super().__init__(msg)
