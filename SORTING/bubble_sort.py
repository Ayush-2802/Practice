arr = list(map(int,input("Enter the array: ").split()))
n = len(arr)

#puts maximum element at last
def bubbleSort(arr):
    for i in range(n-1,0,-1):
        #adjacent swap
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
#time comlexity
# BigO(n^2) - worst and average


# optimize if the array is sorted 
# if thats the case no swap will happen
# so we use a flag swap if its happening or niot to limit the case

def bubbleSortOptimized(arr):
    for i in range(n-1,0,-1):
        swap = 0
        #adjacent swap
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
                swap +=1
        if swap == 0:
            break

bubbleSortOptimized(arr)
print(arr)


# recursive approach