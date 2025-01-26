def check(nums):
    # Count rotations (number of times next element is less than current)
    rotations = 0
    n = len(nums)
    
    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:
            rotations += 1
    
    # If rotations > 1, it means array cannot be sorted by rotation
    return rotations <= 1