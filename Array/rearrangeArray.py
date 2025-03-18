from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n    # Initialize array with zeros, not empty list
        pos = 0
        neg = 1
        for i in range(n):
            if nums[i] > 0:
                res[pos] = nums[i]
                pos+=2
            elif nums[i] < 0:
                res[neg] = nums[i]
                neg+=2
        
        return res

    # Alternative approach using separate arrays first
    def rearrangeArraySafer(self, nums: List[int]) -> List[int]:
        pos = [x for x in nums if x > 0]  # collect positive numbers
        neg = [x for x in nums if x < 0]  # collect negative numbers
        
        # Check if we have equal numbers of each
        if len(pos) != len(neg):
            return nums  # or handle unequal cases differently
            
        result = []
        for i in range(len(pos)):
            result.append(pos[i])  # add positive
            result.append(neg[i])  # add negative
            
        return result