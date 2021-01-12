from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Dict
from typing import Generic
from typing import List
from typing import TypeVar

from ...protocols import Factory
from ...protocols import ParserMap
from ...utils.annotations import field_is_generic_dict
from ...utils.annotations import field_is_generic_list
from ...utils.annotations import get_cls_annotations
from ...utils.annotations import get_primary_inner_type
from .exceptions import AnnotatedDictFieldError
from .exceptions import AnnotatedFieldError
from .exceptions import AnnotatedListFieldError
from .exceptions import MissingAnnotatedField
from .exceptions import MissingAnnotation

T = TypeVar("T")


@dataclass
class AnnotationsParser(Generic[T]):
    cls: Factory[T]
    field_defaults: Dict = field(default_factory=dict)
    field_mappings: Dict = field(default_factory=dict)
    specified_parsers: ParserMap = field(default_factory=dict)

    def __call__(self: T, config: Dict) -> T:
        """
        Parses an object based on its class annotations

        Args:
            config (Dict): Configuration to parse

        Returns:
            T: Parsed object
        """
        parser_kwargs = self.field_defaults.copy()

        for raw_field_name, raw_field_value in config.items():
            field_name = self.match_field_name(raw_field_name)
            field_parser = self.select_field_parser(field_name)
            parser_kwargs[field_name] = self.parse_field(field_parser, raw_field_value)

        for field_name in self.annotations:
            if field_name not in parser_kwargs:
                raise MissingAnnotatedField(field_name, parser_kwargs)

        return self.cls(**parser_kwargs)

    @property
    def annotations(self) -> Dict:
        return get_cls_annotations(self.cls)

    def match_field_name(self, raw_field_name: str) -> str:
        if raw_field_name in self.annotations:
            return raw_field_name

        if raw_field_name in self.field_mappings:
            return self.field_mappings[raw_field_name]

        raise MissingAnnotation(raw_field_name, self.annotations)

    def select_field_parser(self, field_name: str) -> Any:
        """
        Selects which parser to use for a given annotated field

        Args:
            field_name (str): Name of the field to parse

        Returns:
            Any: Selected parser to use
        """
        annotated_type = self.annotations[field_name]
        return (
            self.specified_parsers[annotated_type]
            if annotated_type in self.specified_parsers
            else annotated_type
        )

    @staticmethod
    def parse_field(field_parser: Any, raw_field_value: Any) -> Any:
        if field_parser is Any:
            return raw_field_value

        if field_is_generic_list(field_parser):
            inner_field_parser = get_primary_inner_type(field_parser)
            try:
                return [
                        inner_field_parser(i) if i is not None else None
                        for i in raw_field_value
                    ]
            except TypeError:
                raise AnnotatedListFieldError(inner_field_parser, raw_field_value)

        if field_is_generic_dict(field_parser):
            inner_field_parser = get_primary_inner_type(field_parser)
            try:
                return {
                        k: inner_field_parser(v) if v is not None else None
                        for k, v in raw_field_value.items()
                    }
            except TypeError:
                raise AnnotatedListFieldError(inner_field_parser, raw_field_value)

        try:
            return field_parser(raw_field_value)

        except TypeError:
            raise AnnotatedFieldError(field_parser, raw_field_value)
