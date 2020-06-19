from typing import Callable, Dict, TypeVar

T = TypeVar("T")
Factory = Callable[..., T]
Parser = Callable[[Dict], T]
ParserMap = Dict[T, Parser[T]]
Validator = Callable[..., bool]
