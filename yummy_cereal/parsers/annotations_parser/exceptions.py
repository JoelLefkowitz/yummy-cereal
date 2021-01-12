from typing import Any
from typing import Dict

from ...utils.prettifiers import prettify_dict
from ..exceptions import ParsingError


class MissingAnnotation(ParsingError):
    def __init__(self, field_name: str, annotations: Dict) -> None:
        msg = "Failed to parse field\nEncountered a field with no matching annotation"
        context = prettify_dict(
            {"Missing annotation": field_name, "Annotations": annotations}
        )
        super().__init__(f"{msg}\n{context}")


class MissingAnnotatedField(ParsingError):
    def __init__(self, field_name: str, annotations: Dict) -> None:
        msg = "Failed to parse field\nNo matching field found or default value provided for an annotation"
        context = prettify_dict(
            {"Missing field": field_name, "Annotations": annotations}
        )
        super().__init__(f"{msg}\n{context}")


class AnnotatedFieldError(ParsingError):
    def __init__(self, field_parser: Any, raw_field_value: Any) -> None:
        msg = "Failed to parse field"
        context = {"Field parser type": field_parser, "Raw field value": raw_field_value}
        super().__init__(f"{msg}\n{context}")


class AnnotatedListFieldError(ParsingError):
    def __init__(self, inner_field_parser: Any, raw_field_value: Any) -> None:
        msg = "Failed to parse list field"
        context = {"Inner field parser type": inner_field_parser, "Raw field value": raw_field_value}
        super().__init__(f"{msg}\n{context}")


class AnnotatedDictFieldError(ParsingError):
    def __init__(self, inner_field_parser: Any, raw_field_value: Any) -> None:
        msg = "Failed to parse dict field"
        context = {"Inner field parser type": inner_field_parser, "Raw field value": raw_field_value}
        super().__init__(f"{msg}\n{context}")
