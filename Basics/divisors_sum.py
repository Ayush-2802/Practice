import math
n = 36 
res = []
for i in range (1,int(math.sqrt(n))):
    if n%i == 0:
        res.append(i)
        if n/i!=i :
            res.append(int(n/i))

print(sorted(res))