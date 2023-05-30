import json
import re
import pandas as pd

from recipe import Recipe
from mealplan import MealPlan
# Read the CSV file into a pandas DataFrame
df = pd.read_csv('data/budgetbytes-recipes.csv')  # Replace with your CSV file path

column_name = 'name'
value = 'pasta 5 ingredient butter tomato sauce'
results = df[df[column_name] == value]


df1 = df.head(5)
list_of_recipes = []
for index, row in df1.iterrows():
      list_of_recipes.append(Recipe(row["name"], row["url"]))



# print(results['name'].values)
# print(results['url'].values)
# list_of_recipes.append(
# Recipe(
#   name = results['name'].values[0],
#   url = results['url'].values[0]
# )
# )

mealplan = MealPlan(recipes=list_of_recipes)
# print(json.dumps(mealplan.get_shopping_basket, indent=4))
# print(mealplan.get_total)
# print(mealplan.get_total_servings)



from rich import console
from dateutil.tz import tzlocal
    
from rich.console import Console
from rich.table import Table


ingredients = Table(show_header=True)
ingredients.add_column("ingredients", justify="right", style="green")
ingredients.add_column("quantity")
ingredients.add_column("unit")
ingredients.add_column("price", style="yellow")
ingredients.add_column("currency")
console = Console()

for ingredient in mealplan.get_shopping_basket:
    ingredients.add_row(
        "{0}".format(ingredient.get('name')),
        "{0}".format(ingredient.get('quantity')),
        "{0}".format(ingredient.get('unit')),
        "{0}".format(ingredient.get('price')),
        "{0}".format(ingredient.get('currency')),
    )
ingredients.add_row(
        "{0}".format('total'),
        "{0}".format(''),
        "{0}".format(''),
        "{0}".format(mealplan.get_total),
        "{0}".format(ingredient.get('currency')),
)
console.print(ingredients)

recipes = Table(show_header=True)
recipes.add_column("name", justify="right", style="purple")
recipes.add_column("description")
recipes.add_column("servings")
recipes.add_column("tags", style="yellow")
recipes.add_column("cost", style="red")

for recipe in list_of_recipes:
    recipes.add_row(
        "{0}".format(recipe.name),
        "{0}".format(recipe.get_description),
        "{0}".format(recipe.get_servings),
        "{0}".format(recipe.get_tags[0:3]),
        "{0}".format(recipe.get_total_cost),
    )
recipes.add_row(
        "{0}".format('total'),
        "{0}".format(''),
        "{0}".format(mealplan.get_total_servings),
        "{0}".format(''),
        "{0}".format(mealplan.get_total),
)
console.print(recipes)
# # Print the results
# print(results['name'].values)
# print(results['url'].values)

# recipe_instance = Recipe(
#   name = results['name'].values[0],
#   url = results['url'].values[0]
# )
# print(recipe_instance.name)
# print(recipe_instance.url)

# recipe_instance.get_ingredients()
# #print(json.dumps(recipe_instance.basket, indent=4, sort_keys=True))
# recipe_instance.get_instructions()
# recipe_instance.get_servings()
# print(json.dumps(recipe_instance.instructions, indent=4, sort_keys=True))


# print(recipe_instance.get_total_cost)
# print(recipe_instance.get_servings)
# print(json.dumps(recipe_instance.get_basket, indent=4, sort_keys=True))
# print(recipe_instance.get_instructions)

#TODO: query recipe using URL and parse with BS4
#TODO: use recipe and scrape sites like woolies or pnp for price of item
#TODO: this will require a database

#TODO: build flask API endpoints