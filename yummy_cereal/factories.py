from dataclasses import dataclass, field
from typing import Any, Dict, Generic, List, Optional, Protocol, Tuple, TypeVar, Union

from .exceptions import AnnotationTypeError, ConfigTypeError, InvalidConfig
from .utils import cls_annotations, inner_type, is_generic_dict, is_generic_list

T = TypeVar("T")

Result = Tuple[bool, str]
DataSet = Dict[str, Any]


class Parser(Protocol[T]):
    def __call__(self, config: Dict) -> T:
        ...


ParserMap = Dict[Any, Parser]


class Validator(Protocol):
    def __call__(self, config: Dict) -> Union[bool, Result]:
        ...


@dataclass
class ValidatedParser(Generic[T]):
    parser: Parser[T]
    validators: List[Validator]

    def __call__(self, config: Dict) -> T:
        self.validate(config)
        return self.parser(config)

    def validate(self, config: Dict) -> None:
        for validator in self.validators:
            if isinstance(result := validator(config), Tuple):
                valid, msg = result
            else:
                valid, msg = result, None

            if not valid:
                raise InvalidConfig(msg, config)


@dataclass
class AnotatedFieldsParser:
    cls: T
    collector_field: Optional[str] = None
    collect_with_names: bool = False
    field_defaults: DataSet = field(default_factory=dict)
    typed_parsers: ParserMap = field(default_factory=dict)

    def __call__(self, config: Dict) -> T:
        if not isinstance(config, dict):
            raise ConfigTypeError(config, dict)

        parsed_fields = {
            field_name: self.parse_field(field_name, field_value)
            for field_name, field_value in self.gather_fields(config).items()
        }
        return self.create_object(parsed_fields)

    def get_field_annotation(self, field_name: str) -> Any:
        annotations = cls_annotations(self.cls)
        return annotations[field_name] if field_name in annotations else None

    def get_type_parser(self, field_annotation: Any) -> Any:
        return (
            self.typed_parsers[field_annotation]
            if field_annotation in self.typed_parsers
            else field_annotation
        )

    def gather_fields(self, config: Dict) -> Dict:
        field_data = self.field_defaults.copy()

        if self.collector_field and self.collector_field not in field_data:
            field_data[self.collector_field] = {}

        for k, v in config.items():
            if self.get_field_annotation(k):
                field_data[k] = v

            elif self.collector_field:
                field_data[self.collector_field][k] = v

        return field_data

    def parse_field(self, field_name: str, field_value: Any) -> Any:
        if field_annotation := self.get_field_annotation(field_name):

            if field_name == self.collector_field and self.collect_with_names:
                field_value = self.parse_names(field_value)

            if field_annotation == Any:
                return field_value

            try:
                if is_generic_list(field_annotation):
                    inner_field_parser = self.get_type_parser(
                        inner_type(field_annotation)
                    )
                    return [inner_field_parser(i) for i in field_value]

                elif is_generic_dict(field_annotation):
                    inner_field_parser = self.get_type_parser(
                        inner_type(field_annotation)
                    )
                    return {k: inner_field_parser(v) for k, v in field_value.items()}

                else:
                    field_parser = self.get_type_parser(field_annotation)
                    return field_parser(field_value)

            except TypeError:
                raise AnnotationTypeError(field_annotation, field_value)
        else:
            return field_value

    def parse_names(self, config: Dict) -> List[Dict]:
        return [
            {
                "name": k,
                **(
                    v
                    if isinstance(v, dict)
                    else {i: None for i in v}
                    if isinstance(v, list)
                    else {v: None}
                    if v is not None
                    else {}
                ),
            }
            for k, v in config.items()
        ]

    def create_object(self, field_values: Dict) -> T:
        obj = self.cls.__new__(self.cls)
        obj.__dict__.update(**field_values)
        return obj
