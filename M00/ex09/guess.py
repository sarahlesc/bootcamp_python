import random


def beginning_game():
	print("This is an interactive guessing game!")
	print("Please enter a number between 1 and 99 to find out the secret number.")
	print("Type 'exit' to end the game.")
	print("Good luck!\n")


def game():
	number = random.randint(1,99)
	attempts = 0
	while (1):
		guess = input("What's your guess between 1 and 99 ?\n")
		attempts += 1
		try:
			guess = int(guess)
			if guess == number:
				if attempts == 1:
					print("Congratulations! You got it on your first try.")
					exit()
				if number == 42:
					print("The answer to the ultimate question of life, the universe and everything is 42.")
				print("Congratulations! You've got it")
				print("You've won in %i attempts." % attempts)
				quit()
			else:
				if guess > number:
					print("Too high!")
				elif guess < number:
					print("Too low!")
		except ValueError:
			if guess == 'exit':
				print("Thanks for playing!")
				exit()
			print("That's not a number")


beginning_game()
game()
