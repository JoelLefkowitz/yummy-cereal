from typing import Any
from typing import Dict
from typing import TypeVar

from typing_extensions import Protocol

T = TypeVar("T")


class Factory(Protocol[T]):
    def __call__(self, *args: Any, **kwargs: Any) -> T:
        ...


class Parser(Protocol[T]):
    def __call__(self, config: Dict) -> T:
        ...


class Serializer(Protocol[T]):
    def __call__(self, obj: T) -> Dict:
        ...


class Validator(Protocol[T]):
    def __call__(self, *args: Any, **kwargs: Any) -> bool:
        ...


ParserMap = Dict[T, Parser[T]]
SerializerMap = Dict[T, Serializer[T]]
