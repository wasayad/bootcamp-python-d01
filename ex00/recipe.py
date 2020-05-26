class Recipe:
    def __init__(self, name, cooking_1v1, cooking_time, ingredients, description, recipe_type):
        self.name = name
        self.cooking_1v1 = cooking_1v1
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ""
        txt = list(txt)
        txt.extend('Name:         ')
        txt.extend(self.name)
        txt.extend("\n")
        txt.extend('cooking_1v1:  ')
        txt.extend(str(self.cooking_1v1))
        txt.extend("\n")
        txt.extend('cooking_time: ')
        txt.extend(str(self.cooking_time))
        txt.extend("\n")
        txt.extend('ingredients:  ')
        txt.extend(str(self.ingredients))
        txt.extend("\n")
        txt.extend('description:  ')
        txt.extend(str(self.description))
        txt.extend("\n")
        txt.extend('recipe_type:  ')
        txt.extend(str(self.recipe_type))
        txt = ''.join(txt)
        return txt
    name = 'cake'
    cooking_1v1 = 2
    cooking_time = 45
    ingredients = {'eggs', 'milk', 'cacao', 'flour'}
    description = 'A good and simple meal'
    recipe_type = 'dessert'