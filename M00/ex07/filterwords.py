import sys

if len(sys.argv) != 3:
	print("ERROR")
	exit()
sentence = sys.argv[1]
words = "".join((char if char.isalpha() else " ") for char in sentence).split()
try:
	nb = int(sys.argv[2])
except ValueError:
	print('ERROR')
	exit()
filtered = []
filtered = [x for x in words if len(x) > nb]
print(filtered)
