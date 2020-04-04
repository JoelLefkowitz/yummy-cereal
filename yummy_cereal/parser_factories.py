from dataclasses import dataclass
from .exceptions import ConfigTypeError, InvalidConfig
from typing import Any, Dict, Generic, List, Optional, Protocol, Tuple, TypeVar, Union
from .utils import cls_annotations

T = TypeVar("T")

Result = Tuple[bool, str]


class Parser(Protocol[T]):
    def __call__(self, config: Any) -> T:
        ...


class Validator(Protocol):
    def __call__(self, config: Any) -> Union[bool, Result]:
        ...


ParserSet = Optional[Dict[str, Parser]]


@dataclass
class ValidatedParser(Generic[T]):
    parser: Parser[T]
    validators: List[Validator]

    def __call__(self, config: Any) -> T:
        self.validate(config)
        return self.parser(config)

    def validate(self, config: Any) -> None:
        for validator in self.validators:
            result = validator(config)
            valid, msg = result if isinstance(result, tuple) else result, None

            if not valid:
                raise InvalidConfig(msg, config)


def annotations_parser_factory(
    cls: T,
    omit_fields: List[str] = [],
    collector_field: Optional[str] = None,
    child_parsers: ParserSet = {},
) -> Parser[T]:
    def anotated_fields_parser(config: Dict) -> T:

        if not isinstance(config, dict):
            raise ConfigTypeError(config, dict)

        annotations = cls_annotations(cls)
        annotated_fields = set(annotations) - set(omit_fields)
        data = {k: v for k, v in config.items() if k in annotated_fields}

        if collector_field:
            data[collector_field] = all(map(config.pop, data))

        field_parsers = annotations.update(child_parsers)
        data = {k: field_parsers["k"](v) for k, v in data.items()}

        obj = cls.__new__()
        obj.update(**data)
        return obj

    return anotated_fields_parser
