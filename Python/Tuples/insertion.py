# Demonstrating tuple insertion operations
# Since tuples are immutable, we create new tuples

# Initial tuple
original_tuple = (1, 2, 3, 4, 5)
print("Original tuple:", original_tuple)

# "Inserting" at the beginning (by creating a new tuple)
new_element = 0
new_tuple = (new_element,) + original_tuple
print("After inserting at beginning:", new_tuple)

# "Inserting" at the end
new_tuple = original_tuple + (6,)
print("After inserting at end:", new_tuple)

# "Inserting" in the middle (converting to list and back to tuple)
middle_position = 3
element_to_insert = 10
temp_list = list(original_tuple)
temp_list.insert(middle_position, element_to_insert)
new_tuple = tuple(temp_list)
print("After inserting in middle:", new_tuple)

# Combining multiple tuples
tuple1 = (1, 2)
tuple2 = (3, 4)
tuple3 = (5, 6)
combined_tuple = tuple1 + tuple2 + tuple3
print("Combined tuples:", combined_tuple)