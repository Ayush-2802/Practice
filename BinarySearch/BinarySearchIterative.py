class Solution:
    def search(self, nums,target):
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                high = mid-1
            else:
                low = mid+1
        return -1
    
# Recursive Binary Search Implementation
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.rec(nums,target,0,len(nums)-1)
        
    def rec(self, nums, target, low, high):
        if low > high:
            return -1
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            return self.rec(nums, target, low, mid-1)
        else:
            return self.rec(nums, target, mid+1, high)

# Test the solution
if __name__ == "__main__":
    solution = Solution()  # Test iterative solution
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(solution.search(nums, target))  # Should print 4
    
    recursive_sol = SolutionRecursive()  # Test recursive solution
    print(recursive_sol.search(nums, target))  # Should print 4