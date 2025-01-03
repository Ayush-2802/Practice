def chai (n):
    def actual (x):
        return x ** n
    return actual

square = chai(2)
cube = chai(3)

print(square(5))
print(cube(5))
