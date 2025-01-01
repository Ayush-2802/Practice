# Demonstrating nested tuples and operations

# Creating nested tuples
coordinates = ((1, 2), (3, 4), (5, 6))
mixed_data = (1, ("a", "b"), (2.5, 3.5), ["x", "y"])

# Accessing elements in nested tuples
print("First coordinate pair:", coordinates[0])
print("X value of second coordinate:", coordinates[1][0])

# Tuple unpacking with nested tuples
(point1, point2, point3) = coordinates
print("Unpacked point2:", point2)

# Nested tuple iteration
for x, y in coordinates:
    print(f"Point: ({x}, {y})")

# Finding elements in nested tuples
if (3, 4) in coordinates:
    print("Point (3, 4) found in coordinates")

# Creating a complex nested structure
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

# Accessing and printing matrix elements
print("\nMatrix:")
for row in matrix:
    print(row)

# Demonstrate tuple methods with nested tuples
print("\nCount of (1, 2):", coordinates.count((1, 2)))
print("Index of (3, 4):", coordinates.index((3, 4)))