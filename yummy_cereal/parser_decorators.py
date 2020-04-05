from .exceptions import ConfigTypeError, ConfigFormatError
from .utils import is_proxy_dict
from functools import wraps
from typing import Any, List, TypeVar, Union, Dict
from .parser_factories import Parser


T = TypeVar("T")


def named_parser(parser_function: Parser[T]) -> Parser[T]:
    @wraps(parser_function)
    def parse_with_name(config: Dict):

        if not is_proxy_dict(config):
            raise ConfigFormatError("{name: {data}, name: [data] ...}", config)

        data = {
            k: {i: {} for i in v} if isinstance(v, list) else v
            for k, v in config.items()
        }

        if len(data) == 1:
            name, data = list(data.items())[0]
            data["name"] = name

        else:
            data = [{"name": k, **v} for k, v in data.items()]

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
