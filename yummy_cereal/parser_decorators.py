from .exceptions import ConfigTypeError, ConfigFormatError
from .utils import is_proxy_dict, first_items
from functools import wraps
from typing import Any, List, TypeVar, Union
from .parser_factories import Parser


T = TypeVar("T")


def named_parser(parser_function: Parser[T]) -> Parser[T]:
    @wraps(parser_function)
    def parse_with_name(config: Any):

        if not is_proxy_dict(config):
            raise ConfigFormatError("{name: {data}}", config)

        name, data = first_items(config)
        data["name"] = name
        return parser_function(data)

    return parse_with_name


def list_parser(parser_function: Parser[T]) -> Parser[List[T]]:
    @wraps(parser_function)
    def parse_list(config: List):

        if not isinstance(config, list):
            raise ConfigTypeError(config, list)

        return [parser_function(i) for i in config]

    return parse_list


def list_or_single_parser(
    parser_function: Parser[T],
) -> Union[Parser[T], Parser[List[T]]]:
    @wraps(parser_function)
    def parse_list(config: Any):

        if not isinstance(config, list):
            return parser_function(config)

        return [parser_function(i) for i in config]

    return parse_list
