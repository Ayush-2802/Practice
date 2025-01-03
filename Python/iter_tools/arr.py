lst = [1,2,3,4]

i = iter(lst)

print(next(i))
print(i.__next__())
print(next(i))
print(i.__next__())