import pytest


@pytest.fixture
def full_menu():
    return {
        "language": "English",
        "courses": {
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
def invalid_menu():
    return {
        "language": "English",
        "courses": {
            "Desserts": ["Cake", "Custard"],
            "Drinks": ["Tea", "Coffee"],
            "Wines": ["Red", "Rose"],
        },
    }
