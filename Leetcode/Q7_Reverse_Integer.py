def reverse(x):
    print(f"Input received: {x}")  # Debug print
    # Constants for 32-bit integer limits
    MIN = -2147483648
    MAX = 2147483647
    
    # Handle negative numbers
    sign = 1
    if x < 0:
        sign = -1
        x = abs(x)
    
    res = 0
    while x:
        digit = x % 10
        x = x // 10
        print(f"Current digit: {digit}, Current res: {res}")  # Debug print
        
        # Check for overflow before adding new digit
        if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
            return 0
            
        res = (res * 10) + digit
    
    final_result = sign * res
    print(f"Final result: {final_result}")  # Debug print
    return final_result

# Test case
if __name__ == "__main__":
    test_input = 1463847412
    result = reverse(test_input)
    print(f"Test case result: {result}")