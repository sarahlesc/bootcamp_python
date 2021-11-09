import sys

sys.path.append(".")

import datetime
from recipe import Recipe

meals = ['starter', 'lunch', 'dessert']

class Book:
	def __init__(self, name):
		# NAME
		try:
			self.name = str(name)
		except ValueError:
			print("the name of the book should be a string.")
			exit()
		# LAST_UPDATE
		self.creation_date = datetime.date.today()
		self.last_update = self.creation_date
		self.recipes_list = {
			'starter': [], 'lunch': [], 'dessert': []
		}

	def get_recipe_by_name(self, name):
		for meal in meals:
			for recipe in self.recipes_list[meal]:
				if recipe.name == name:
					print(str(name))
					return recipe


	def get_recipe_by_types(self, recipe_type):
		for key in self.recipes_list:
			if recipe_type == key:
				print(self.recipes_list[recipe_type])
				return key
		print('this recipe type does not exist')
		exit()


	def add_recipe(self, recipe):
		if type(recipe) == Recipe:
			self.recipe_list[recipe.recipe_type].append(recipe)
			last_update = datetime.date.today
		else:
			print('This is not a Recipe')
			exit()
