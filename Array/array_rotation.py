arr = list(map(int,input("Enter the array").split()))
n = len(arr)
d=3

def left_rotation(arr,n,d):
    temp = arr[0:d]
    for j in range(d,n):
        arr[j-d] = arr[j]

    for i in range(n-d,n):
        arr[i] = temp[i-(n-d)]
    
    return arr
    
print(left_rotation(arr,n,d))

#rotate right
# Step 1: Reverse the last k elements of the array
# Step 2: Reverse the first n-k elements of the array.
# step 3: Reverse the whole array.

def rev(arr,start,end):
    while start<end:
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1

def right_rotate(arr,n,d):
    d = k % n
    rev(arr,0,n-d-1)
    rev(arr,n-d,n-1)
    rev(arr,0,n-1)

