import math

n = 7789
res = 0

# l = math.log10(n)+1
# print(int(l))

rev = 0
if n < 0:
    rev += -1
while n > 0:
    res = int(n%10)
    n = int(n/10)
    rev = (rev*10)+res

print(rev)