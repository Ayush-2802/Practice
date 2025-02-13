N = 7789
n = N
res = 0
c = 0
while n > 0:
    res = int(n%10)
    n = int(n/10)
    if N%res == 0:
        c += 1
print(c)

    
