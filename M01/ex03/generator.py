import random


def generator(text, sep=" ", option=None):
	try:
		check_text = isinstance(text, str)
		split_text = text.split(sep)
		if option != None:
			if option == 'shuffle':
				new_s = []
				j = 0
				while j < len(split_text):
					i = random.randint(0, len(split_text) - 1)
					new_s.append(split_text[i])
					split_text.remove(split_text[i])
				split_text = new_s
			elif option == 'unique':
				new_s = dict.fromkeys(split_text)
				split_text = new_s
			elif option == 'ordered':
				new_s = []
				new_s = sorted(split_text)
				split_text = new_s
			else:
				print("Wrong option given. 3 options available : shuffle, unique and ordered")
				exit()
		for i in split_text:
			yield i
	except:
		print("ERROR")
		exit()
