import collections

def divideArrayBrute(nums):
    nums = sorted(nums)    # O(nlogn) time
    n = len(nums)
    res = 0
    for i in range(0,n,2):  # O(n) time
        if nums[i] == nums[i+1]:
            res+=1
    return res == n/2

def divideArrayOptimal(nums):
    c = collections.Counter(nums)  # O(n) time
    for i in c.values():          # O(k) time, k = unique elements
        if i%2 == 1:
            return False
    return True

# Method 1: Using XOR (Most optimal for memory)
def divideArrayXOR(nums):
    xor = 0
    freq = {}
    for num in nums:
        xor ^= num        # XOR all numbers
        freq[num] = freq.get(num, 0) + 1    # Count frequencies
    return xor == 0 and all(v % 2 == 0 for v in freq.values())

# Method 2: Using Set (Most optimal for time)
def divideArraySet(nums):
    seen = set()
    for num in nums:
        if num in seen:
            seen.remove(num)
        else:
            seen.add(num)
    return len(seen) == 0

# Method 3: Using array (if numbers are in small range)
def divideArrayArray(nums):
    freq = [0] * (max(nums) + 1)  # If we know range is small
    for num in nums:
        freq[num] ^= 1  # Toggle between 0 and 1
    return sum(freq) == 0

def divideArrayBetter(nums):
    seen = {}
    for num in nums:
        seen[num] = seen.get(num, 0) + 1
    return all(count % 2 == 0 for count in seen.values())

