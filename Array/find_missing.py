def findMissing(nums):
    n = len(nums)
    x1 = 0
    x2 = 0
    for i in range(n):
        x2 ^= nums[i]
        x1 ^= (i+1)
    x1 ^= n
    return x1^x2

nums = list(map(int, input("Enter array elements: ").split()))
print("Missing number:", findMissing(nums))