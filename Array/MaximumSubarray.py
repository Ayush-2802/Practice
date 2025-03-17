def MaximumSubarray(nums):
    m = float('-inf')
    s = 0

    for i in nums:
        s +=i
        if s>m:
            m = s
        if s<0:
            s=0
    
    return m
    