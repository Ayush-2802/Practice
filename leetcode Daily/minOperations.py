class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        x = set(nums)
        count = 0
        if min(x) < k:
            return -1
        
        for num in x:
            if num > k:
                count += 1
        return count