import sys

sys.path.append(".")

from book import Book
from recipe import Recipe

burger = Recipe('burger', 2, 60, {'bread', 'tomato', 'steak', 'cheese', 'onions', 'ketchup'}, 'Put everything together', 'lunch')
to_print = str(burger)
print(to_print)
#print(lasagna.recipe_type)

italian = Book('Italian food')

italian.get_recipe_by_name('burger')

#italian.get_recipe_by_types('lunch')

italian.add_recipe('burger')
