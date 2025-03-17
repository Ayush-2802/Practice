def longestSubarray(arr,n,k):  # optimal for +ve , -ve
    d = {}
    preSum = 0
    maxLen = 0
    for i in range(n):
        preSum += arr[i]
        if preSum == k : maxLen = max(maxLen,i+1)
        rem = preSum - k
        if rem in d:
            newLen = i - d.get(rem)
            maxLen = max(maxLen,newLen)
        if preSum not in d:
            d[preSum] = i

    return maxLen



def longsubarr(arr,n,k):
    left = 0
    right = 0
    s = arr[0]
    l = 0

    while right < n:
        while(left <= right and s > k):
            s -= arr[left]
            left += 1
        if s == k:
            l = max(l,right-left+1)
        right += 1
        if right < n :
            s += arr[right]

    return l

arr = list(map(int,input("enter the array: ").split()))
k = int(input("Enter the value Of K: "))
n = len(arr)

print(longsubarr(arr,n,k))