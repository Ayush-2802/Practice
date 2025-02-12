def get_divisors_sum(x):
    
    div_sum = 0
    i = 1
    
    # Only need to check up to square root of x
    while i * i <= x:
        if x % i == 0:
            div_sum += i
            # If i is not the square root, add the pair divisor
            if i != x // i:
                div_sum += x // i
        i += 1
    
    return div_sum

def get_total_sum(n):
    
    total = 0
    
    for i in range(1, n + 1):
        total += get_divisors_sum(i)
    
    return total

# Get input and calculate result
n = int(input("enter the number :"))
print(get_total_sum(n))
