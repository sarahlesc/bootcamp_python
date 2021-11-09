cookbook = {
        'sandwich': {'ingredients': ["ham", "bread", "cheese", "tomatoes"], 'meal': 'lunch', 'prep_time': '10'},
        'cake': {'ingredients': ["flour", "sugar", "eggs"], 'meal': 'dessert', 'prep_time': '60'},
        'salad': {'ingredients': ["avocado", "arugula", "tomatoes", "spinach"], 'meal': 'lunch', 'prep_time': '15'}}


def print_recipe(recipe):

    print("Recipe for %s:" % recipe)
    print(f"Ingredients list: {cookbook[recipe]['ingredients']}")
    print("To be eaten for %s" % cookbook[recipe]['meal'])
    print("Takes %s minutes of cooking" % cookbook[recipe]['prep_time'])


def delete_recipe(recipe):
    del cookbook[recipe]


def add_new_recipe(recipe, ingredients, meal, prep_time):
	words_ingredients = ingredients.split(", ")
	cookbook[recipe] = {'ingredients': words_ingredients, 'meal': meal, 'prep_time': prep_time}
	print_recipe(recipe)

def print_all_recipes(cookbook):
    for key in cookbook:
        print_recipe(key)
    return


def beginning_cookbook():
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    choice = input('\n')
    while (1):
        if choice == '1':
            new_recipe = input("Name of the recipe :\n")
            new_ingredients = input("Ingredients :\n")
            new_meal = input("Type of meal :\n")
            new_prep_time = input("Preperation time :\n")
            add_new_recipe(new_recipe, new_ingredients, new_meal, new_prep_time)
        elif choice == '2':
            deleted_recipe = input("Which recipe would you like to delete ?\n")
            if deleted_recipe in cookbook:
                delete_recipe(deleted_recipe)
            else:
                print("ERROR: this recipe does not exist")
        elif choice == '3':
            printed_recipe = input("Which recipe would you like to print ?\n")
            if printed_recipe in cookbook:
                print_recipe(printed_recipe)
            else:
                print("ERROR: this recipe does not exist")
        elif choice == '4':
            print_all_recipes(cookbook)
        elif choice == '5':
            print("Cookbook closed")
            exit()
        else:
            print("This option does not exist, please type the corresponding number.")
        choice = input('\n')


beginning_cookbook()
