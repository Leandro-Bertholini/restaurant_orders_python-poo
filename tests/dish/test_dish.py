from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    dish_ravioli = Dish('ravioli', 18.99)
    dish_lasanha = Dish('lasanha', 26.99)
    gorgonzola = Ingredient("queijo gorgonzola")
    creme_de_leite = Ingredient("creme_de_leite")

    assert dish_ravioli.name == 'ravioli'
    assert dish_lasanha.name == 'lasanha'

    assert dish_lasanha.price == 26.99
    assert dish_ravioli.price == 18.99

    assert dish_lasanha != dish_ravioli

    assert dish_lasanha.recipe == {}

    assert dish_ravioli.__repr__() == "Dish('ravioli', R$18.99)"

    assert dish_ravioli.__hash__() == dish_ravioli.__hash__()
    assert dish_ravioli.__hash__() != dish_lasanha.__hash__()

    dish_lasanha.add_ingredient_dependency(gorgonzola, 3)
    dish_lasanha.add_ingredient_dependency(creme_de_leite, 3)

    assert dish_lasanha.recipe == {gorgonzola: 3, creme_de_leite: 3}

    assert dish_lasanha.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }

    assert dish_lasanha.get_ingredients() == {gorgonzola, creme_de_leite}

    assert dish_lasanha == Dish('lasanha', 26.99)

    with pytest.raises(TypeError):
        Dish('lasanha', '26.99')

    with pytest.raises(ValueError):
        Dish('lasanha', -26.99)
