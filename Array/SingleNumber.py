def SingleNumber(arr):
    x = 0
    for i in range(len(arr)):
        x ^= arr[i]
    return x

arr = list(map(int, input("Enter array elements: ").split()))
print("Missing number:", SingleNumber(arr))