arr = list(map(int,input("Enter the array:").split()))
n = len(arr)

def insertionSort(arr):
    for i in range(n): 
        j = i
        while(j>0 and arr[j-1]>arr[j]):
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j -= 1

insertionSort(arr)
print(arr)