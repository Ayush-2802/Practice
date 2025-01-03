class Solution:  # Remove (object) as it's not needed in Python 3
    def productExceptSelf(self, nums: List[int]) -> List[int]:  # Add type hints
        res = [1] * len(nums)
        
        # Calculate prefix products
        prefix = 1
        for i, num in enumerate(nums):  # Use enumerate instead of range
            res[i] = prefix
            prefix *= num
            
        # Calculate suffix products
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
            
        return res
