# Creating a list
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

# 1. Updating single element using index
my_list[2] = 10
print("After updating single element:", my_list)

# 2. Extending list with another list
my_list.extend([6, 7, 8])
print("After extending:", my_list)

# 3. Appending single element
my_list.append(9)
print("After appending:", my_list)

# 4. Inserting element at specific position
my_list.insert(1, 15)
print("After inserting at index 1:", my_list)

# 5. Updating multiple elements using slice
my_list[2:4] = [20, 25]
print("After updating slice:", my_list)

# 6. Adding lists using +
my_list = my_list + [30, 35]
print("After concatenation:", my_list)

# 7. Removing elements
my_list.remove(15)  # removes first occurrence of 15
print("After removing 15:", my_list)

# 8. Pop element at index
popped = my_list.pop(2)
print(f"Popped {popped}, new list:", my_list)

# 9. Clear entire list
my_list.clear()
print("After clearing:", my_list)

# 10. Reinitialize list and demonstrate replacement
my_list = [1, 2, 3, 4, 5]
print("New list:", my_list)

# Replace elements using slice with different length
my_list[1:4] = [10, 20]
print("After replacing multiple elements with fewer:", my_list)

# Replace single element with multiple elements
my_list[0:1] = [100, 200, 300]
print("After replacing one element with multiple:", my_list)