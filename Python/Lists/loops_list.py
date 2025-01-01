lst = ["Chicken", "Mutton", "Fish", "Prawns", "Crab"]

for i in lst:
    print(i, end=" ")

sq = [x**2 for x in range(10)]
print(sq) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]