class Recipe:
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
		# NAME
		try:
			self.name = str(name)
		except ValueError:
			print("the name of the recipe should be a string.")
			exit()
		# COOKING_LVL
		try:
			self_cooking_lvl = int(cooking_lvl)
			if self_cooking_lvl >= 1 & self_cooking_lvl <= 5:
				self.cooking_lvl = self_cooking_lvl
			else:
				print("cooking_lvl sould be ranged between 1 and 5.")
				exit()
		except ValueError:
			print('cooking_lvl sould be an integer ranged between 1 and 5.')
			exit()
		# COOKING_TIME
		try:
			self_cooking_time = int(cooking_time)
			if self_cooking_time > 0:
				self.cooking_time = self_cooking_time
			else:
				print("cooking_time shoud be a positive integer.")
				exit()
		except ValueError:
			print("cooking_time should be a positive integer.")
			exit()
		# INGREDIENTS
		self_ingredients = list(ingredients)
		for i in self_ingredients:
			if len(i) == 1:
				print('ingredients should be a list.')
				exit()
		self.ingredients = self_ingredients
		# DESCRIPTION
		try:
			self_description = str(description)
			if description == None or description == '':
				if description == None:
					description = ""
				self.description = str(description)
			self.description = str(description)
		except ValueError:
			print('description should be a string')
			exit()
		# RECIPE_TYPE
		try:
			self_recipe_type = str(recipe_type)
			if self_recipe_type == 'starter' or self_recipe_type == 'lunch' or self_recipe_type == 'dessert':
				self.recipe_type = self_recipe_type
			else:
				print('recipe_type should only be starter, lunch or dessert')
				exit()
		except ValueError:
			print("recipe_type should be a string: 'starter', 'lunch' or 'dessert'")
			exit()


	def __str__(self):
		txt = f"{self.name} is for {self.recipe_type}.\n" \
		f"The degree of diffculty is {self.cooking_lvl} out of 5.\n" \
		f"You need {self.cooking_time} minutes and {self.ingredients} to do it.\n" \
		f"{self.description}"
		return txt
