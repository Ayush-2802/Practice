# The intersection() method will return a new set, that only contains the items that are present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
set3 = set1 & set2 # works only with sets
set1.intersection_update(set2) # The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

print(set3)

