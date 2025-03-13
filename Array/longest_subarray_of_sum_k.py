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



def longsubarr(arr,k,n):
    pass

arr = list(map(int,input("enter the array: ").split()))
k = int(input("Enter the value Of K: "))
n = len(arr)

print(longestSubarray(arr,n,k))

