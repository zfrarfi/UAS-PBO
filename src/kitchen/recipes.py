"""Simple recipe data model for kitchen/cooking mechanics."""
from dataclasses import dataclass
from typing import List, Tuple

# A step is (action, duration_seconds). Actions: 'cut', 'boil', 'fry', 'brew', 'assemble', 'serve'
Step = Tuple[str, float]

@dataclass
class Recipe:
    name: str
    ingredients: List[str]
    steps: List[Step]
    price: int


# Example recipes
RECIPES = {
    "Coffee": Recipe(
        name="Coffee",
        ingredients=["Water", "Coffee Beans"],
        steps=[("brew", 3.0), ("serve", 0.5)],
        price=5,
    ),
    "Tea": Recipe(
        name="Tea",
        ingredients=["Water", "Tea Bag"],
        steps=[("boil", 2.5), ("serve", 0.5)],
        price=4,
    ),
    "Sandwich": Recipe(
        name="Sandwich",
        ingredients=["Bread", "Cheese", "Lettuce"],
        steps=[("assemble", 2.0), ("serve", 0.5)],
        price=8,
    ),
    "Cake": Recipe(
        name="Cake",
        ingredients=["Flour", "Sugar", "Egg"],
        steps=[("mix", 3.0), ("bake", 6.0), ("serve", 0.5)],
        price=7,
    ),
    "Juice": Recipe(
        name="Juice",
        ingredients=["Water", "Fruit"],
        steps=[("blend", 2.0), ("serve", 0.5)],
        price=6,
    ),
}

def get_recipe(name: str) -> Recipe:
    return RECIPES.get(name)
