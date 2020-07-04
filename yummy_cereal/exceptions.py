from typing import Any


class ValidationFailed(Exception):
    def __init__(self, obj: Any) -> None:
        msg = f"The given object data failed a validation check\n{obj}"
        super().__init__(msg)


class FieldParsingError(Exception):
    def __init__(self, field_parser: Any, raw_field_value: Any) -> None:
        msg = f"Failed to parse field\nParser: {field_parser}\nField value: {raw_field_value}"
        super().__init__(msg)


class ListFieldParsingError(Exception):
    def __init__(self, inner_field_parser: Any, raw_field_value: Any) -> None:
        msg = f"Failed to parse list field\nInner parser: {inner_field_parser}\nField value: {raw_field_value}"
        super().__init__(msg)


class DictFieldParsingError(Exception):
    def __init__(self, inner_field_parser: Any, raw_field_value: Any) -> None:
        msg = f"Failed to parse dict field\nInner parser: {inner_field_parser}\nField value: {raw_field_value}"
        super().__init__(msg)


class MissingFieldError(Exception):
    def __init__(self, obj: Any, field_name: str) -> None:
        msg = f"Failed to serialize object\nMissing field name: {field_name}\nObject: {obj}"
        super().__init__(msg)


class ListFieldSerializingError(Exception):
    def __init__(self, field_data: Any, inner_field_serializer: Any) -> None:
        msg = f"Failed to serialize list field\nInner serializer: {inner_field_serializer}\nField_data: {field_data}"
        super().__init__(msg)


class DictFieldSerializingError(Exception):
    def __init__(self, field_data: Any, inner_field_serializer: Any) -> None:
        msg = f"Failed to serialize dict field\nInner serializer: {inner_field_serializer}\nField_data: {field_data}"
        super().__init__(msg)
