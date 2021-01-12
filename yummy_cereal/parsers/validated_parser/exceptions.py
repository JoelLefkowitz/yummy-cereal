from typing import Any

from ...utils.prettifiers import prettify_dict
from ..exceptions import ParsingError


class ParserValidationFailed(ParsingError):
    def __init__(self, obj: Any) -> None:
        msg = "The given object data failed a parser validation check"
        context = prettify_dict({"Given object": obj})
        super().__init__(f"{msg}\n{context}")
