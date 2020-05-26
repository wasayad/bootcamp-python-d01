from vector import Vector

v1 = Vector(3)
v2 = Vector([0.0, 1.0, 2.0, 3.0])
v3 = Vector((10, 14))
print(v1.values)
print(v2.values)
print(v3.values)
v4 = v3 - v2
print(v4.values)
v4 = v3 / v2
print(v4.values)
v4 = v3 + v2
print(v4.values)
v4 = v3 * v2
print(v4.values)
print(v4.__str__())
print(v4.__repr__())
