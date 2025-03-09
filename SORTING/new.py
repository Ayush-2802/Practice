arr = [4, 1, 3, 9, 7]
n = len(arr)

def sel(arr):
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                arr[i] , arr[j] = arr[j] , arr[i]


def bub(arr):
    for i in range(n):
        swap = False
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
        if swap == False:
            break

def ins(arr):
    for i in range(n): 
        j = i
        while(j>0 and arr[j-1]>arr[j]):
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j -= 1


print(arr)
ins(arr)
print(arr)