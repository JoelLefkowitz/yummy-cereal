from .utils.prettifiers import prettify_dict


class FieldParsingError(Exception):
    def __init__(self, field_parser: Any, raw_field_value: Any) -> None:
        msg = "Failed to parse field\n" + prettify_dict(
            {"Parser": field_parser, "Field value": raw_field_value}
        )
        super().__init__(msg)


class ListFieldParsingError(FieldParsingError):
    def __init__(self, inner_field_parser: Any, raw_field_value: Any) -> None:
        super().__init__(inner_field_parser, raw_field_value)


class DictFieldParsingError(FieldParsingError):
    def __init__(self, inner_field_parser: Any, raw_field_value: Any) -> None:
        super().__init__(inner_field_parser, raw_field_value)


class ParserValidationFailed(Exception):
    def __init__(self, obj: Any) -> None:
        msg = (
            "The given object data failed a parser validation check\n"
            + prettify_dict({"Given object": obj})
        )
        super().__init__(msg)
