from src.models.dish import Dish
from src.models.ingredient import Ingredient
import csv


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()

        with open(source_path, "r") as csv_file:
            file = csv.DictReader(csv_file)

            for row in file:
                dish = row["dish"]
                price = float(row["price"])
                ingredient = row["ingredient"]
                recipe_amount = int(row["recipe_amount"])

                # cria cada objeto e adiciona ao conjunto
                self.dishes.add(Dish(dish, price))

                # para iterar
                next_dish = next(iter(self.dishes))

                next_dish.add_ingredient_dependency(
                    Ingredient(ingredient), recipe_amount
                )
