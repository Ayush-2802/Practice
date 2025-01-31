# Given an array of integers, find and print all subarrays whose sum equals zero

arr = [1,-1,2,-2,3,4,5]

for i in range(len(arr)):
    for j in range(i, len(arr)):
        subarray_sum = sum(arr[i:j+1])
        if subarray_sum == 0:
            print(f"{arr[i:j+1]}", end=":")



class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left + 1, right + 1]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1