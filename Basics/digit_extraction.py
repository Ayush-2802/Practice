import math

n = -7789
res = 0

# l = math.log10(n)+1
# print(int(l))

rev = 0
while n < 0:
    res = n%10
    n = n/10
    rev = (rev*10)+res

print(rev)