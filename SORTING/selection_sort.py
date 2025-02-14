arr = list(map(int, input("Enter array elements separated by space: ").split()))
l = len(arr)

def selectionSort(arr):
    for i in range(l):
        min_ele = i
        for j in range(i+1,l):
            if arr[j] < arr[min_ele]: min_ele = j
        arr[i] , arr[min_ele] = arr[min_ele] , arr[i]

selectionSort(arr)
print(arr)

