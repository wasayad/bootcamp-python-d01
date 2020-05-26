from book import Book
from recipe import Recipe

cookbook = Book('cookbook')

toadd = Recipe('tarte', 2, 45, 'eggs', 'good', 'dessert')
cookbook.add_recipe(toadd)
toadd = Recipe('tourte', 2, 45, 'eggs', 'good', 'dessert')
cookbook.add_recipe(toadd)
cookbook.get_recipe_by_name(toadd)
print(cookbook.get_recipes_by_types('dessert'))
print(cookbook.creation_date)
print(cookbook.last_update)