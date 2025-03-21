class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        brp = -1
        n = len(nums)
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                brp = i
                break

        if brp == -1:
            nums.reverse()
            return
            
        for i in range(n-1, brp, -1):
            if nums[i] > nums[brp]:
                nums[i], nums[brp] = nums[brp], nums[i]
                break
                
        # Use slice assignment with reverse
        nums[brp+1:] = nums[brp+1:][::-1]        

        