import unittest
from yummy_cereal import ValidatedParser, InvalidConfig


class TestParserDecorators(unittest.TestCase):
    def test_ValidatedParser(self) -> None:
        parser = ValidatedParser(
            parser=int, validators=[lambda x: isinstance(x, str), lambda x: x.isdigit()]
        )
        self.assertEqual(parser("1"), 1)
        self.assertNotEqual(parser("2"), 1)
        self.assertRaises(InvalidConfig, parser, 3)

    def test_annotations_parser_factory(self) -> None:
        pass
