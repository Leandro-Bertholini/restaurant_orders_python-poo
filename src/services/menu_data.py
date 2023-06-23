from src.models.dish import Dish
from src.models.ingredient import Ingredient
import csv


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self._dishes = set()

        with open(source_path, "r") as csv_file:
            file = csv.DictReader(csv_file)

            for row in file:
                dish = row["dish"]
                price = float(row["price"])
                ingredient = row["ingredient"]
                recipe_amount = int(row["recipe_amount"])

                self.dishes.add(Dish(dish, price))

                # o iterador é criado internamente no conjunto self.dishes
                dish = self.dishes

                dish.add_ingredient_dependency(
                    Ingredient(ingredient), recipe_amount
                )
