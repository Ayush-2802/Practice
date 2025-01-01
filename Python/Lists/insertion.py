my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

# 1. append() - adds element at the end
my_list.append(6)
print("After append(6):", my_list)

# 2. insert() - adds element at specific index
my_list.insert(2, 10)
print("After insert(2, 10):", my_list)

# 3. extend() - adds multiple elements at the end
my_list.extend([7, 8, 9])
print("After extend([7, 8, 9]):", my_list)

# 4. Using + operator to concatenate lists
my_list = my_list + [11, 12]
print("After concatenation:", my_list)

# 5. Using slice assignment
my_list[1:1] = [15, 16]
print("After slice insertion:", my_list)

# 6. Multiple insertion using *= operator
small_list = [1, 2]
small_list *= 3
print("After multiplication:", small_list)

# String list examples
fruits = ['apple', 'banana']
print("\nString list operations:")
print("Original fruits:", fruits)

# Adding strings
fruits.append('orange')
print("After append:", fruits)

# Inserting at beginning
fruits.insert(0, 'grape')
print("After insert at start:", fruits)

# Extending with multiple fruits
fruits.extend(['mango', 'kiwi'])
print("After extend:", fruits)

# inset nothiong
lstx = [1, 2, 3, 4, 5]
lstx[1,3] = []
print(lstx) # [1, 4, 5]