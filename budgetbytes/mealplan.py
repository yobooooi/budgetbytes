from cgitb import reset
import itertools
import json

from recipe import Recipe
from typing import List


class MealPlan:

    @property
    def get_shopping_basket(self):
        return self._shopping_basket

    @property
    def get_total(self):
        return round(self._total_cost, 2)

    @property
    def get_total_servings(self):
        return self._total_servings

    def __init__(self, recipes: List[Recipe]) -> None:
        self.recipes = recipes
        self._shopping_basket = []
        self._total_cost = 0
        self._total_servings = 0
        self._set_shopping_list()

    def _update_basket(self, ingredients_from_recipe):
        for ingredient in ingredients_from_recipe:
            if not any(item['name'] == ingredient.get('name') for item in self._shopping_basket):
                self._shopping_basket.append(ingredient)
            else:
                for item in self._shopping_basket:
                    if item['name'] == ingredient.get('name'):
                        item['quantity'] += ingredient.get('quantity')
                        item['price'] += ingredient.get('price')

    def _set_shopping_list(self):
        for recipe in self.recipes:
            self._update_basket(recipe.get_basket)
            self._total_cost += recipe.get_total_cost
            self._total_servings += recipe.get_servings