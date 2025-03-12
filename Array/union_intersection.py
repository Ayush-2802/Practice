a = list(map(int,input("enter the array: ").split()))
b = list(map(int,input("enter the array: ").split()))

def union(a,b):
    return sorted(set(a)|set(b))
def intersection(a,b):
    return sorted(set(a)&set(b))


def missingNumber(nums: List[int]) -> int:
        n = len(nums)
        temp = list(range(n))
        res = set(temp) - set(nums)
        return res