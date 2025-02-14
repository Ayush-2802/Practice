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


# Time complexity analysis
# n+(n-1)+(n-1)+....2+1 
# (n * n+1)/2
# n**2/n + n/2
# BigO(n^2) - Best,Worst,Avg
