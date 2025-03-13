def brute(arr,t):
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j] == t:
                return [i,j]

def better(arr,t):
    hashmem = {}
    for i in range(len(arr)):
        neednum = t - arr[i]
        if neednum in hashmem:
            return [i,hashmem.get(neednum)]
        hashmem[arr[i]] = i

arr = list(map(int,input("enter the array: ").split()))
t = int(input("enter the target: "))
res = better(arr,t)
print(res)