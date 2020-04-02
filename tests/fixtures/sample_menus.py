import pytest


@pytest.fixture
def full_menu():
    return {
        "Language": "English",
        "Courses": {
            "Appetizers": ["Fruit", "Muesli"],
            "Mains": [
                {"Pastas": ["Penne", "Bow-tie"]},
                {"Pizzas": ["Margarita", "Farmhouse"]},
            ],
            "Desserts": ["Cake", "Custard"],
            "Drinks": ["Tea", "Coffee"],
            "Wines": ["Red", "Rose"],
        },
    }


@pytest.fixture
def simple_menu():
    return {
        "Language": "English",
        "Courses": {
            "Appetizers": None,
            "Mains": None,
            "Desserts": None,
            "Drinks": None,
            "Wines": None,
        },
    }


@pytest.fixture
def implicit_names_menu():
    return {
        "Language": "English",
        "Appetizers": None,
        "Mains": None,
        "Desserts": None,
        "Drinks": None,
        "Wines": None,
    }


@pytest.fixture
def nested_fields_menu():
    return {
        "Language": "English",
        "Appetizers": ["Fruit", "Muesli"],
        "Mains": [
            {"Pastas": ["Penne", "Bow-tie"]},
            {"Pizzas": ["Margarita", "Farmhouse"]},
        ],
        "Desserts": None,
        "Drinks": None,
        "Wines": None,
    }