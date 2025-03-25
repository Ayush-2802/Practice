arr = list(map(int,input("Enter the array:").split()))
n = len(arr)

def merge(arr,low,mid,high):

    temp = []
    left = low
    right = mid+1

    while( left<=mid and right<=high):
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1

    while (left<=mid):
        temp.append(arr[left])
        left+=1
    
    while (right<=high):
        temp.append(arr[right])
        right+=1
    
    for i in range(len(temp)):
        arr[low+i] = temp[i]

def merge_sort(arr,low,high):
    if low == high : return
    mid = (low+high)//2
    merge_sort(arr,low,mid)
    merge_sort(arr,mid+1,high)
    merge(arr,low,mid,high)

print(arr)
merge_sort(arr,0,n-1)
print(arr)


arr = list(map(int,input("Enter the number").split()))
n = len(arr)

def merge(arr,low,mid,high):
    temp = []
    left = low
    right = mid+1

    while left<=mid and right<=high:
        if arr[left<=arr[right]]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while left<=mid:
        temp.append(arr[left])
        left += 1

    while right<=high:
        temp.append(arr[right])
        right += 1

    for i in range (len(temp)):
        arr[low+1] = temp[i]

def merge_sort(arr,low,high):
    if low == high : return
    mid = (low+high)//2
    merge_sort(arr,low,mid)
    merge_sort(arr,mid+1,high)
    merge(arr,low,mid,high)


class Solution:
    
    def merge(self,arr,low,mid,high):
        temp = []
        left = low
        right = mid+1
        
        while left<=mid and right<=high:
            if left<=low:
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                right+=1
        
        while left<=mid:
            temp.append(arr[left])
            left+=1
            
        while right<=high:
            temp.append(arr[right])
            right+=1
        
        for i in range(len(temp)):
            arr[low+1] = temp[i]
            
            
    def mergeSort(self,arr, low, high):
        #code here
        if low == high : return
        mid = (low+high)//2
        self.mergeSort(arr,low,mid)
        self.mergeSort(arr,mid+1,high)
        self.merge(arr,low,mid,high)
        

def merge(arr,low,mid,high):
    temp = []
    left = low
    right  =  mid+1

    while left<=mid and right <= high:
        if left <= low:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right += 1

    while left<=mid:
        temp.append(arr[left])
        left+=1

    while right<=high:
        temp.append(arr[right])
        right += 1

    for i in range(len(temp)):
        arr[low+1] = temp[i]

def mergeSort(arr,low,high):
    if low == high:
        return
    mid = (low+high)//2
    mergeSort(arr,low,mid)
    mergeSort(arr,mid+1,high)
    merge(arr,low,mid,high)

