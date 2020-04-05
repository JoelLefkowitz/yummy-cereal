from dataclasses import dataclass, field
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


@dataclass
class AnotatedFieldsParser:
    cls: T
    collector_field: Optional[str] = None
    omit_fields: List[str] = field(default_factory=list)
    child_parsers: ParserSet = field(default_factory=dict)

    def __call__(self, config: Dict) -> T:

        if not isinstance(config, dict):
            raise ConfigTypeError(config, dict)

        return self.create_object(self.extract(config))

    @property
    def annotations(self) -> Dict:
        annots = cls_annotations(self.cls)
        annots.update(self.child_parsers)
        return annots

    @property
    def annotated_fields(self) -> List[str]:
        return (
            self.annotations.keys()
            if not self.omit_fields
            else list(set(self.annotations) - set(self.omit_fields))
        )

    def extract(self, config) -> Dict:
        obj_data = {self.collector_field: {}} if self.collector_field else {}

        for k, v in config.items():
            if k in self.annotated_fields:
                obj_data[k] = v

            elif self.collector_field:
                obj_data[self.collector_field][k] = v

        if self.annotations:
            obj_data = {k: self.annotations[k](v) for k, v in obj_data.items()}

        return obj_data

    def create_object(self, obj_data: Dict) -> T:
        obj = self.cls.__new__(self.cls)
        obj.__dict__.update(**obj_data)
        return obj
