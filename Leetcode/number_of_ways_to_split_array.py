sum_l = 0
sum_r = sum(nums)
split_count = 0

for i in range(len(nums)-1):
    sum_l += nums[i]
    sum_r -= nums[i]
    if sum_l >= sum_r:
        split_count +=1
    
print(split_count)