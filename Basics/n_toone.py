n = int(input())

def n_to_one(i,n):
    if i<n:
        print(i)
    n_to_one(i-1,n)

n_to_one(n,n)
