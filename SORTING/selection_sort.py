arr = list(map(int, input("Enter array elements separated by space: ").split()))
l = len(arr)

def selectionSort(arr):
    for i in range(l):
        first = i
        min_ele = i
        for j in range(i+1,l):
            if arr[j] < arr[min_ele]:
                min_ele = j
                arr[first] , arr[min_ele] = arr[min_ele] , arr[first]

selectionSort(arr)
print(arr)

