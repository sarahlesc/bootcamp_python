from generator import generator

text = "Le Lorem Ipsum est simplement du faux texte."

print("NO OPTION:")
for word in generator(text, sep=" "):
	print(word)

print("\nSHUFFLE:")
for word in generator(text, sep=" ", option="shuffle"):
	print(word)

print("\nORDERED:")
for word in generator(text, sep=".", option="ordered"):
	print(word)

print("\nUNIQUE :")
text = "Lorem Ipsum Lorem Ipsum"
for word in generator(text, sep=" ", option="unique"):
	print(word)

print("\nErreurs : ")
text = 1.0
for word in generator(text, sep="."):
	print(word)
