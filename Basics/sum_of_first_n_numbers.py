def sum_n(n: int) -> int:
    # Base case
    if n <= 1:
        return n
    
    # Recursive case: n + sum of first (n-1) numbers
    return n + sum_n(n-1)

# Get input and print result
n = int(input())
print(sum_n(n))