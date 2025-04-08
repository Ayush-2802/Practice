from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        
        for num in nums1:
            # Find position of num in nums2
            i = 0
            while i < len(nums2) and nums2[i] != num:
                i += 1
                
            # Find next greater element
            greater = -1
            for j in range(i+1, len(nums2)):
                if nums2[j] > num:
                    greater = nums2[j]
                    break
            
            result.append(greater)
        
        return result