# Union
# The union() method returns a new set with all items from both sets.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) 
set3 = set2 | set1 # You can use the | operator instead of the union() method, and you will get the same result.

# multiple set join
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4

# Join a Set and a Tuple
tup1 = (1,2,3,4)
myset2 = set1 | tup1