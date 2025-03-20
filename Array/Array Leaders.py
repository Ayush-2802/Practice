class Solution:
    def leaders(self, nums):
        # code here
        #brute
        res = []
        m = float("-inf")
        
        for i in range(len(nums)-1,-1,-1):
            if nums[i] >= m:
                res.append(nums[i])
            m = max(m,nums[i])
            
        return reversed(res)