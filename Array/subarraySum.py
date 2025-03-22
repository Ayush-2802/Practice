def subarraySumBrute(nums,n,k):
    d = 0
    for i in range(n):
        for j in range(i+1,n+1):
            if sum(nums[i:j]) == k:
                d+=1
    return d

def subarraySumOptimal(nums,n,k):
    d = {}
    preS = 0
    c = 0
    d[preS] = 1

    for i in range(n):
        preS+=nums[i]
        remove = preS-k
        c += d[remove]
        d[preS] += 1
    
    return c