import sys

if len(sys.argv) != 2:
    print("ERROR")
    exit()
try:
    nb = int(sys.argv[1])
except ValueError:
    print("ERROR")
    exit()
nb = int(sys.argv[1])
if nb == 0:
    print("I'm Zero.")
else:
    remainder = nb % 2
    if remainder != 0:
        print("I'm Odd.")
    else:
        print("I'm Even.")
