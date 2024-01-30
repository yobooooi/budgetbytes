from flask import Flask


app = Flask(__name__)
#TODO: figure out how to scrape, cache and query data from woolies and checkers

# Architecture and technologies
#TODO: design architecture and considerations for technologies

# Presentation
#TODO: what front end and framewok
#TODO: presentation of meal plans
#TODO: should this perhaps be an android or apple application ?
#TODO: how would users interact with app. UCook should be a good example

# API considerations
# HTTP endpoints need to model the budegtbytes-recipe.csv the recipe class
# is called to firstly retrieve the ingredients from the URLS but data is used
# to enrich the csv data. perhaps the cache is a field on the record or the 
# record is enriched as a batch job
#TODO: determine HTTP methods and endpoints
#TODO: recipe ID for cached recipes
#TODO: endpoint receives json object. ensure syntax
#TODO: searching. ask ChatGPT for querying data using pandas

# Integration consideration
#TODO: figure out how to integrate with apps to create baskets

# Data enrichment considerations
#TODO: how to enrich data, adding meta data to recipes
#TODO: run through entire database and enrich data with the ingredients
#
# breakfast, lunch, dinner
# ingredients, allergents, preferences: vegetarian and vegan
# pricing
# caloric count
#
@app.route("/recipe")
def index():
    return "This is yet another version!"