n = int(input())
def fact(n):
    if n == 0 or n == 1 or n == 2 : return n
    else : return n*fact(n-1)

print(fact(n))