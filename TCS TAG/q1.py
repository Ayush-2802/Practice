#q1 easy
def generate_decorations(n, b, c, a):
    result = []
    
    def backtrack(current, rem_b, rem_c, rem_a):
        if len(current) == n:
            result.append(current)
            return
        # Try each possible accessory in order B, C, A
        if rem_b > 0:
            backtrack(current + 'B', rem_b - 1, rem_c, rem_a)
        if rem_c > 0:
            backtrack(current + 'C', rem_b, rem_c - 1, rem_a)
        if rem_a > 0:
            backtrack(current + 'A', rem_b, rem_c, rem_a - 1)
    
    backtrack("", b, c, a)
    return result

# Example usage:
n = 2
b = 0
c = 1
a = 1
output = generate_decorations(n, b, c, a)
print(' '.join(output))  # Output: CA AC