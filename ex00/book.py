import datetime
from recipe import Recipe
class Book:
    def __init__(self, name):
        self.name = name
        self.last_update = datetime.datetime.now()
        self.creation_date = datetime.datetime.now()
        self.recipes_list = {
            'starter' : [],'lunch': [],'dessert': []
        }
    name = ""
    last_update = datetime.datetime.now()
    creation_date = datetime.datetime.now()
    recipes_list = {
        'starter' : [],'lunch': [],'dessert': []
    }
    def get_recipe_by_name(self, name):
        print(str(name))
    def get_recipes_by_types(self, recipe_type):
        return(self.recipes_list[recipe_type])
    def add_recipe(self, recipe):
        if isinstance(recipe, Recipe) is False:
            return(print("Error, this is not a valid recip."))
        typ = recipe.recipe_type
        nam = recipe.name
        self.recipes_list[typ].append(nam)
        self.last_update = datetime.datetime.now()

