from vector import Vector

V1 = Vector([0.0, 1.0, 2.0, 3.0])
V2 = Vector([1.1, 2.2, 3.3, 4.4])

print("\nROW VECTOR\n")
print("\naddition of a row\n")
V1.__add__(V2)
V1.__radd__(V2)

print("\nsubstraction of a row\n")
V1.__sub__(V2)
V1.__rsub__(V2)

print("\ndivision of a row\n")
V1.__truediv__(2)
V1.__rtruediv__(2)

print("\nmultiplication of a row\n")
V1.__mul__(2)
V1.__rmul__(2)

print("\ntranspose and dot operations on a row\n")
V1.__dot__(V2)
V1.T()

print("COLUMN VECTOR")

V3 = Vector([[0.0], [1.0], [2.0], [3.0]])
V4 = Vector([[0.1], [1.1], [2.2], [3.3]])

print("\naddition of a column\n")
V3.__add__(V4)
V3.__radd__(V4)

print("\nsubstraction of a column\n")
V3.__sub__(V4)
V3.__rsub__(V4)

print("\ndivision of a column\n")
V3.__truediv__(4)
V3.__rtruediv__(4)

print("\nmultiplication of a column\n")
V3.__mul__(2)
V3.__rmul__(2)

print("\ntranspose and dot operations on a column\n")
V3.__dot__(V4)
V3.T()

print("\n __STR__ AND __REPR__\n")
print("__str__ =")
to_print = str(V2)
print(to_print)
print("__repr__ =")
to_print = repr(V2)
print(to_print)

print("\nEXAMPLES SUBJECT\n")
V2.__shape__()
print(V2.T().shape)
