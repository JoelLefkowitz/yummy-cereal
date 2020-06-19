import json
from typing import Any

import ruamel.yaml


def from_yaml(path: str) -> Any:
    """ 
    Reads input from a yaml file

    Args:
        path (str): Path of yaml file

    Returns:
        Any: Contents of yaml file
    """
    with open(path, "r") as stream:
        return ruamel.yaml.load(stream, Loader=ruamel.yaml.Loader)


def to_yaml(path: str, output: Any) -> None:
    """
    Writes output to yaml file

    Args:
        path (str): Output path
        output (Any): Content to output
    """
    with open(path, "w") as stream:
        ruamel.yaml.dump(output, stream, Loader=ruamel.yaml.Loader)


def from_json(path: str) -> Any:
    """ 
    Reads input from a json file

    Args:
        path (str): Path of json file

    Returns:
        Any: Contents of json file
    """
    with open(path, "r") as stream:
        return json.load(stream)


def to_json(path: str, output: Any) -> None:
    """
    Writes output to json file

    Args:
        path (str): Output path
        output (Any): Content to output
    """
    with open(path, "w") as stream:
        return json.dump(output, stream)
