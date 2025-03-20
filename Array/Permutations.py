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


def rec(ind, nums, ans):
    if ind == len(nums):
        ans.append(nums[:])  # Directly append a copy of nums
        return

    for i in range(ind, len(nums)):
        nums[i], nums[ind] = nums[ind], nums[i]  # Swap
        rec(ind+1, nums, ans)  # Corrected function call
        nums[i], nums[ind] = nums[ind], nums[i]  # Swap back

def permuteII(nums):
    ans = []
    rec(0, nums, ans)
    return ans

# Example usage
nums = [1, 2, 3]
print(permuteII(nums))