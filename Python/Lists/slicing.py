# List slicing demonstration
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing [start:end] (end is exclusive)
print("Original list:", numbers)
print("First three elements:", numbers[0:3])  # [0, 1, 2]
print("Elements from index 4 to 7:", numbers[4:7])  # [4, 5, 6]

# Using negative indices
print("Last three elements:", numbers[-3:])  # [7, 8, 9]
print("All elements except last two:", numbers[:-2])  # [0, 1, 2, 3, 4, 5, 6, 7]

# Using step [start:end:step]
print("Every second element:", numbers[::2])  # [0, 2, 4, 6, 8]
print("Every third element:", numbers[::3])  # [0, 3, 6, 9]

# Reverse the list
print("Reversed list:", numbers[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Slicing with negative step
print("Every second element from end:", numbers[::-2])  # [9, 7, 5, 3, 1]

# Omitting indices
print("From start to index 5:", numbers[:5])  # [0, 1, 2, 3, 4]
print("From index 5 to end:", numbers[5:])  # [5, 6, 7, 8, 9]