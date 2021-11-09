import sys

if len(sys.argv) < 3:
    print("Usage: python operations.py <number1> <number2>")
    print("Example:\n  python operations.py 10 3")
    exit()
if len(sys.argv) > 3:
    print("Usage: too many arguments\n")
    print("Usage : python operations.py <number1> <number2>")
    print("Example:\n  python operations.py 10 3")
    exit()
try:
    nb_1 = int(sys.argv[1])
    nb_2 = int(sys.argv[2])
except ValueError:
    print("InputError: only numbers\n")
    print("Usage: python operations.py <number1> <number2>")
    print("Example:\n  python operations.py 10 3")
    exit()


def mathematic_operations(nb_1, nb_2):
    sum = nb_1 + nb_2
    print("Sum:         %i" % sum)
    difference = nb_1 - nb_2
    print("Difference:  %i" % difference)
    product = nb_1 * nb_2
    print("Product:     %i" % product)
    if nb_2 == 0:
        print("Quotient:    ERROR (div by zero)")
        print("Remainder:   ERROR (modulo by zero)")
    else:
        quotient = nb_1 / nb_2
        remainder = nb_1 % nb_2
        print("Quotient:   ", quotient)
        print("Remainder:  ", remainder)
    return


mathematic_operations(nb_1, nb_2)
