items = ["apple", "banana", "orange", "apple", "mango"]
unique_items = []

for item in items:
    if item not in unique_items:
        print(item)
        break
    unique_items.append(item)
