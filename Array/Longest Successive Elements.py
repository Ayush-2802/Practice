from typing import List

def longestSuccessiveElements(a: List[int]) -> int:
    # Write your code here.
    #optimal
    n = len(a)
    if n == 0 : return 0
    
    s = set(a)
    lon = 0
    
    for i in s:
        # Only start counting if i is the start of a sequence
        if i - 1 not in s:
            c = 1
            x = i
            while x + 1 in s:
                x += 1
                c += 1
            lon = max(lon, c)
    return lon