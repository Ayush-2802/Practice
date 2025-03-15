def sortColors(self, nums: List[int]) -> None:
    c0 = 0
    c1 = 0
    c2 = 0
    
    for i in nums:
        if i == 0:
            c0 += 1
        elif i == 1:
            c1 += 1
        elif i == 2:
            c2 += 1
    
    # Fill array with correct counts
    for i in range(0, c0):
        nums[i] = 0
    for j in range(c0, c0+c1):
        nums[j] = 1    # Changed i to j
    for k in range(c0+c1, len(nums)):
        nums[k] = 2    # Changed i to k


def dutchNationalFlagAlgo(arr,n):
    low ,mid ,high = 0
    while(mid<=high):
        if arr[mid] == 0:
            arr[low] , arr[mid] = arr[mid] , arr[low]
            low += 1
            mid+=1

        elif arr[mid] == 1:
            mid+=1

        else :
            arr[mid] , arr[high] = arr[high] ,arr[mid]
            high -= 1