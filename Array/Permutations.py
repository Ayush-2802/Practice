class Solution:
    def rec(self,nums,ds,ans,freq):
        if len(ds) == len(nums):
            ans.append(ds[:])
            return

        for i in range(len(nums)):
            if not freq[i]:
                freq[i] = True
                ds.append(nums[i])
                self.rec(nums,ds,ans,freq)
                ds.pop()
                freq[i] = False
             
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ds = []
        freq = [False] * len(nums)
        self.rec(nums,ds,ans,freq)
        return ans

# Example usage
nums = [1, 2, 3]
solution = Solution()
print(solution.permute(nums))