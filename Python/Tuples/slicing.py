# Creating a sample tuple
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Basic slicing examples
print("Original tuple:", numbers)
print("First three elements:", numbers[:3])
print("Last three elements:", numbers[-3:])
print("Elements from index 2 to 5:", numbers[2:6])
print("Every second element:", numbers[::2])
print("Reverse the tuple:", numbers[::-1])
print("Elements from index 3 to 7 with step 2:", numbers[3:8:2])
print("Elements from start to 5 (exclusive):", numbers[:5])
print("Elements from 5 to end:", numbers[5:])
print("Middle portion of tuple:", numbers[3:-3])