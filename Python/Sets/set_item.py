# Set Items 
# Set items are unordered, unchangeable, and do not allow duplicate values.

thisset = {"apple", "banana", "cherry", "apple"}
# thisset = {"apple", "banana", "cherry", True, 1, 2} # True and 1 is considered the same value:
# thisset = {"apple", "banana", "cherry", False, True, 0} # False and 0 is considered the same value:

print(len(thisset))

set1 = {"abc", 34, True, 40, "male"} # A set with strings, integers and boolean values:

set2 = set(("apple", "banana", "cherry")) # note the double round-brackets (set constructor)