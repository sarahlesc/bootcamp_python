from vector import Vector

V1 = Vector([0.0, 1.0, 2.0, 3.0])
V2 = Vector([1.1, 2.2, 3.3, 4.4])

print("V1")
V1.__add__(V2)
V1.__sub__(V2)
V1.__truediv__(2)
V1.__mul__(2)
V1.__dot__(V2)
V1.T()

print("V3")
V3 = Vector([[0.0], [1.0], [2.0], [3.0]])
V4 = Vector([[0.1], [1.1], [2.2], [3.3]])
V3.__add__(V4)
V3.__sub__(V4)
V3.__truediv__(4)
V3.__mul__(2)
V3.__dot__(V4)
V3.__repr__()
V3.T()

to_print = str(V2)
print(to_print)
to_print = repr(V2)
print(to_print)

print("EXAMPLES SUBJECT")
V2.__shape__()

print(V2.T().shape)
