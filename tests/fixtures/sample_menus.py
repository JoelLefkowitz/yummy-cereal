import pytest


@pytest.fixture
def full_menu():
    return {
        "Language": "English",
        "Courses": {
            "Appetizers": ["Fruit", "Muesli"],
            "Mains": {
                "Pasta": {"shapes": ["Penne", "Bow-tie"]},
                "Pizza": {"toppings": ["Margarita", "Farmhouse"]},
            },
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
        "Mains": {
            "Pasta": {"shapes": ["Penne", "Bow-tie"]},
            "Pizza": {"toppings": ["Margarita", "Farmhouse"]},
        },
        "Desserts": None,
        "Drinks": None,
        "Wines": None,
    }


@pytest.fixture
def single_course_menu():
    return {
        "name": "Mains",
        "Pasta": {"shapes": ["Penne", "Bow-tie"]},
        "Pizza": {"toppings": ["Margarita", "Farmhouse"]},
    }


@pytest.fixture
def single_dish_menu():
    return {
        "Pasta": {"details": {"shapes": ["Penne", "Bow-tie"]}},
    }


@pytest.fixture
def simple_dishes_menu():
    return [
        {"name": "Pasta", "details": {"shapes": ["Penne", "Bow-tie"]}},
        {"name": "Pizza", "details": {"toppings": ["Margarita", "Farmhouse"]}},
    ]


@pytest.fixture
def simple_single_dish_menu():
    return {"name": "Pasta", "details": {"shapes": ["Penne", "Bow-tie"]}}
