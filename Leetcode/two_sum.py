for i in range(len(nums)):
    for j in range (i+1,len(nums)):
        if nums[i]+nums[j] == target:
            return [i,j]

seen = {}
for i ,n in enumerate(nums):
    c = target-n
    if c in seen:
        return [seen[c],i]
    seen[n] = i 