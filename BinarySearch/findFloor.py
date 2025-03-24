class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self, arr, x):
        #Your code here
        low = 0
        high = len(arr) - 1
        ans = len(arr)
        
        while low<=high:
            mid = low + (high-low) // 2
            if arr[mid] >= x:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        x = int(input().strip())
        ob = Solution()
        ans = ob.findFloor(arr, x)
        print(ans)
        tc -= 1

# } Driver Code Ends







import bisect
class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self, arr, x):
        #Your code here
        return bisect.bisect_left(arr,x)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        x = int(input().strip())
        ob = Solution()
        ans = ob.findFloor(arr, x)
        print(ans)
        tc -= 1

# } Driver Code Ends


#User function Template for python3
import bisect
class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        arr.sort()
        floor_pos = bisect.bisect_right(arr, x)
        if floor_pos == 0:
            floor = -1
        else:
            floor = arr[floor_pos - 1] 
        
        ceil_pos = bisect.bisect_left(arr, x)
        if ceil_pos == len(arr):
            ceil = -1 
        else:
            ceil = arr[ceil_pos]
            
        return [floor, ceil]