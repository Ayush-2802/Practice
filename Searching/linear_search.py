arr = list(map(int,input("enter the array: ").split()))
x = int(input("enter element to be found: "))
n = len(arr)

def Linear_search(arr,n,x):
    for i in range(n):
        if arr[i] == x:
            return i
    return -1

print(Linear_search(arr,n,x))
