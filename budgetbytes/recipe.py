import codecs
import requests
import os
import re

from bs4 import BeautifulSoup

from lib.parse_ingredients import parse_ingredient
from lib.formatters import valid_string


class Recipe:
    @property
    def get_total_cost(self):
        return round(self._total_cost, 2)
    
    @property
    def get_servings(self):
        return self._servings
    
    @property
    def get_basket(self):
        return self._basket

    @property
    def get_instructions(self):
        return self._instructions

    @property
    def get_description(self):
        return self._description

    @property
    def get_tags(self):
        return self._tags

    def __init__(self, name, url) -> None:
        self.name = name
        self.url = url
        self._description = ""
        self._basket = []
        self._instructions = {}
        self._total_cost = 0
        self._servings = 0
        self._tags = []

        self._set_ingredients()
        self._set_instructions()
        self._set_servings()
        self._set_tags()

    def _cache(function):
        # headers for to prevent CDN from blocking requests.get method
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        }
        cache_directory = "./data/cache/"

        def wrap_function(self, *args, **kwargs):
            # removing white spaces for a valid file name to cache the web page for later use
            file_name = f"{re.sub('[^A-Za-z0-9]+', '', self.name)}.html"
            cached_file = os.path.join(cache_directory, file_name)
            if os.path.isfile(cached_file):
                soup_file = codecs.open(cached_file, "r", "utf-8")
                soup_tree = BeautifulSoup(soup_file.read(), "html.parser")
            else:
                response = requests.get(self.url, headers=headers)
                with open(f'{cached_file}', 'w') as file_to_cache:
                    file_to_cache.writelines(response.text)
                soup_tree = BeautifulSoup(response.content, "html.parser")

            recipe_content = soup_tree
            kwargs['recipe_content'] = recipe_content
            return function(self, *args, **kwargs)

        return wrap_function

    @_cache
    def _set_ingredients(self, *args, **kwargs):
        recipe_content = kwargs['recipe_content']
        ingredients = recipe_content.find_all("li", class_="wprm-recipe-ingredient")
        for ingredient in ingredients:
            description, amount = ingredient.text.strip().rsplit(" ", 1)
            self._total_cost += float(amount.strip(")(").strip('$'))
            try:
                ingrendient_component = parse_ingredient(description)
                formatted_ingredient_component_name = valid_string(ingrendient_component.name)
                self._basket.append({
                    "name": formatted_ingredient_component_name,
                    "quantity": ingrendient_component.quantity,
                    "unit": ingrendient_component.unit,
                    "price": float(amount.strip(")(").strip('$')),
                    "currency": "$"
                })
            except IndexError:
                formatted_ingredient_description_name = valid_string(description)
                self._basket.append({
                    "name": formatted_ingredient_description_name,
                    "quantity": 1.0,
                    "price": 0.0,
                    "currency": "$"
                })

    @_cache
    def _set_instructions(self, *args, **kwargs):
        recipe_content = kwargs['recipe_content']
        instructions = recipe_content.find_all("div", class_="wprm-recipe-instruction-text")
        for index, instruction in enumerate(instructions, start=1):
            self._instructions[index] = instruction.text.strip()

    @_cache
    def _set_servings(self, *args, **kwargs):
        recipe_content = kwargs['recipe_content']
        element = recipe_content.find(attrs={"data-servings": True})
        if element is not None:
            self._servings = float(element['data-servings'])

    @_cache
    def _set_tags(self, *args, **kwargs):
        recipe_content = kwargs['recipe_content']
        category_links = recipe_content.find_all('a', {'rel' : 'tag'})
        self._tags = [link.get_text(strip=True) for link in category_links]