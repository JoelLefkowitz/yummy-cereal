from typing import Any, Dict, List, Callable, Optional, Tuple
from exceptions import InvalidStructure, UnparsedConfig
from dataclasses import dataclass


@dataclass
class NamedParser:
    name: str
    parser: Optional[Callable]

    def parse(self, dct: Dict) -> Tuple[Any, Dict]:
        dct_copy = dct.copy()
        value = dct_copy.pop(self.name, None)
        parsed_value = self.parser(value, dct_copy) if self.parser else value
        return parsed_value, dct_copy


class StageParser:
    parser_attributes: List[NamedParser]
    named_children: NamedParser

    def __init__(self, name: str, config: Any) -> None:
        self.name = name

        if isinstance(config, Dict) and self.parse_attributes:
            config = self.parse_attributes(config)

        if config and self.named_children:
            config = self.parse_children(config)

        if config:
            raise UnparsedConfig(config)

    def parse_attributes(self, config: Dict) -> Dict:
        for child in self.parser_attributes:
            child_value, config = child.parse(config)
            setattr(self, child.name, child_value)
        return config

    def parse_children(self, config: Any) -> Any:

        if self.named_children.parser is None:
            children = config

        elif isinstance(config, Dict):
            children = [self.named_children.parser(k, v) for k, v in config.items()]

        elif isinstance(config, List[Dict]):
            children = [
                self.named_children.parser(k, v) for i in config for k, v in i.items()
            ]

        else:
            raise InvalidStructure(config)

        setattr(self, self.named_children.name, children)

    def __repr__(self):
        return str(self.__dict__)
