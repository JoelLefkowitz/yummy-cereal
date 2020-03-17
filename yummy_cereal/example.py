import ruamel.yaml
from parse import StageParser, NamedParser


def read(config_path: str) -> dict:
    """
    Read configuration from yaml file
    
    Args:
        config_path (str): Path to configuration file
    
    Returns:
        Any: Unvalidated configuration
    """
    with open(config_path, "r") as stream:
        return ruamel.yaml.load(stream, Loader=ruamel.yaml.Loader)


class SizedDish(StageParser):
    parser_attributes = [NamedParser("size", None)]
    named_children = None


class LongDish(StageParser):
    parser_attributes = [NamedParser("alt-name", None), NamedParser("flavours", None)]
    named_children = None


class MainCatagory(StageParser):
    parser_attributes = []
    named_children = NamedParser("dishes", SizedDish)


class DessetCatagory(StageParser):
    parser_attributes = []
    named_children = NamedParser("dishes", LongDish)


class Menu(StageParser):
    parser_attributes = [NamedParser("desserts", DessetCatagory)]
    named_children = NamedParser("mains", MainCatagory)


if __name__ == "__main__":
    import os
    from pprint import pprint

    config_path = os.path.normpath(os.path.join(__file__, "../../tests/spec.yml"))
    config = read(config_path)
    menu = Menu("name", config)

    pprint(menu)
