def numpr(n):
    # Base case
    if n < 1:
        return
    
    # Recursive call with n-1 first
    numpr(n-1)
    
    # Print current number
    print(n)

# Get input and call function
n = int(input())
numpr(n)
