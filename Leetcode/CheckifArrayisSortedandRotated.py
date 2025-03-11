n = len(arr)
c =1

for i in range(1,2*n):
    if nums[(i-1)%n] <= nums[i%n]:
        c += 1
    else : c = 1
    if c == n : return True
return n == 1