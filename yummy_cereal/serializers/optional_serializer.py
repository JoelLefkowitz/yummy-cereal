# TODO 
# from dataclasses import dataclass
# from typing import Dict, Generic, Optional, TypeVar

# from ..protocols import serializer
# from .exceptions import FieldParsingError

# T = TypeVar("T")


# @dataclass
# class Optionalserializer(Generic[T]):
#     serializer: serializer[T]

#     def __call__(self, config: Dict) -> Optional[T]:
#         try:
#             return self.serializer(config)
#         except FieldParsingError:
#             return None
