a = list(map(int,input("enter the array: ").split()))
b = list(map(int,input("enter the array: ").split()))

def union(a,b):
    return sorted(set(a)|set(b))
def intersection(a,b):
    return sorted(set(a)&set(b))


def missingNumber(nums: List[int]) -> int:
    n = len(nums)
    # Expected sum of numbers from 0 to n
    expected_sum = (n * (n + 1)) // 2
    # Actual sum of numbers in array
    actual_sum = sum(nums)
    # Missing number is the difference
    return expected_sum - actual_sum