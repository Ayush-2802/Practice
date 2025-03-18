from typing import List

class Solution:
    # Original solution - Two pointers, single pass
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pos = 0
        neg = 1
        
        for i in range(n):
            if nums[i] > 0:
                res[pos] = nums[i]
                pos += 2
            else:
                res[neg] = nums[i]
                neg += 2
        
        return res
    
    # Optimize for readability and intent
    def rearrangeArrayClear(self, nums: List[int]) -> List[int]:
        result = []
        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x < 0]
        
        for p, n in zip(pos, neg):  # Use zip instead of range(len())
            result.extend([p, n])   # Add both elements at once
            
        return result
    
    # Optimize for speed (list comprehension)
    def rearrangeArrayFast(self, nums: List[int]) -> List[int]:
        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x < 0]
        
        # Interleave in one line using list comprehension
        return [x for pair in zip(pos, neg) for x in pair]
    
    # Optimize for memory (in-place rearrangement using O(1) extra space)
    def rearrangeArrayInPlace(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Count positive numbers
        pos_count = sum(1 for num in nums if num > 0)
        
        # Create a copy to avoid overwriting during rearrangement
        temp = nums.copy()
        
        # Set indices
        pos_idx, neg_idx = 0, 1
        
        # Place numbers in result array
        for num in temp:
            if num > 0:
                nums[pos_idx] = num
                pos_idx += 2
            else:
                nums[neg_idx] = num
                neg_idx += 2
                
        return nums

    # Alternative approach using separate arrays first
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x < 0]
        res = []
        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])
        
        return res