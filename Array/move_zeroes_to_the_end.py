arr = list(map(int,input("enter the array: ").split))
n = len(arr)

for i in range(n):
    for j in range(i+1,n):
        if arr[i] == 0:
            arr[i] , arr[j] = arr[j] , arr[i]
        

nonZero = 0

for i in range(n):
    if arr[i] != 0:
        arr[nonZero] , arr[i] = arr[i] , arr[nonZero]
        nonZero += 1