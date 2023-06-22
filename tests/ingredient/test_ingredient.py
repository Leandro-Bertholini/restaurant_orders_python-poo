from src.models.ingredient import Ingredient, restriction_map  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient_one = Ingredient("frango")
    ingredient_two = Ingredient("camarão")
    ingredient_three = Ingredient("frango")

    assert ingredient_one.name == "frango"

    # Retorna hashes iguais
    assert hash(ingredient_one) == hash(ingredient_three)

    # Retorna hashes diferentes
    assert hash(ingredient_one) != hash(ingredient_two)

    assert ingredient_one == ingredient_three

    assert ingredient_two != ingredient_three

    expected_restrictions = restriction_map().get("camarão", set())
    assert ingredient_two.restrictions == expected_restrictions

    assert ingredient_three.__repr__() == "Ingredient('frango')"
