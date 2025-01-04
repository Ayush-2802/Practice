# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
set3 = set1 - set2 # works only with sets
set1.difference_update(set2) # The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.

print(set3)