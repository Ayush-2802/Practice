
arr = list(map(int, input("Enter the array: ").split()))
n = len(arr)

def part(arr,low,high):
    pivot = arr[low]
    i = low
    j = high

    while(i<j):
        while (arr[i]<= pivot and i<=high-1):
            i+=1
        while (arr[j] >= pivot and j>low):
            j-=1
        
        if i<j :
            arr[i] , arr[j] = arr[j] , arr[i]
    
    arr[low] , arr[j] = arr[j] , arr[low]
    return j

def quick_sort(arr,low,high):
    if (low<high):
        p = part(arr,low,high)
        quick_sort(arr,low,p-1)
        quick_sort(arr,p+1,high)

quick_sort(arr,0,n-1)
print(arr)