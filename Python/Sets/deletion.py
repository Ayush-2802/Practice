# To remove an item in a set, use the remove(), or the discard() method.

#remove()
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#discard()
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
# If the item to remove does not exist, discard() will NOT raise an error.

# Remove a random item by using the pop() method:
# pop()
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
# Sets are unordered, so when using the pop() method, you do not know which item that gets removed

# empties the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)