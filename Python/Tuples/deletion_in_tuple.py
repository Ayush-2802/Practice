# Create a sample tuple
my_tuple = (1, 2, 3, 4, 5)
print("Original tuple:", my_tuple)

# Convert to list to delete elements and then convert back to tuple
temp_list = list(my_tuple)
temp_list.remove(3)  # Remove specific element
new_tuple = tuple(temp_list)
print("After removing 3:", new_tuple)

# Delete entire tuple
del my_tuple
# print(my_tuple)  # This would raise NameError because tuple is deleted

# Creating new tuple by slicing (excluding elements)
another_tuple = (1, 2, 3, 4, 5)
# Remove element at index 2
modified_tuple = another_tuple[:2] + another_tuple[3:]
print("After removing element at index 2:", modified_tuple)