from .exceptions import ConfigTypeError
from functools import wraps
from typing import Any, List, TypeVar, Union
from .parser_factories import Parser


T = TypeVar("T")


def named_parser(parser_function: Parser[T]) -> Parser[T]:
    @wraps(parser_function)
    def parse_with_name(config: Any):

        if not isinstance(config, dict):
            raise ConfigTypeError(config, dict)

        name, data = config
        data["name"] = name
        return parser_function(data)

    return parse_with_name


def list_parser(parser_function: Parser[T]) -> Parser[List[T]]:
    @wraps(parser_function)
    def parse_list(config: List):

        if not isinstance(config, list):
            raise ConfigTypeError(config, list)

        for i in config:
            return parser_function(i)

    return parse_list


def list_or_single_parser(
    parser_function: Parser[T],
) -> Union[Parser[T], Parser[List[T]]]:
    @wraps(parser_function)
    def parse_list(config: List):

        if not isinstance(config, list):
            return parser_function(config)

        for i in config:
            return parser_function(i)

    return parse_list
