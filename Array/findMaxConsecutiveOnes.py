def findMaxConsecutiveOnes(nums):
    count = 0    # current streak of ones
    max_count = 0    # maximum streak found so far
    
    for num in nums:
        if num == 1:
            count += 1    # increment current streak
            max_count = max(max_count, count)    # update max if needed
        else:
            count = 0    # reset streak when we see 0
    
    return max_count

# Get input
nums = list(map(int, input("Enter binary array (0s and 1s): ").split()))
print("Maximum consecutive ones:", findMaxConsecutiveOnes(nums))