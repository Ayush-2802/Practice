# Real-World Example: Multiprocessing for CPU-bound Tasks
# Scenario: Factorial Calculation
# Factorial calculations, especially for large numbers, involve significant computational work. 
# Multiprocessing can be used to distribute the workload across multiple
# CPU cores, improving performance.

import multiprocessing
import math
import sys
import time

# increasing the max number of digits for in conversion
sys.set_int_max_str_digits(100000)

# function to compute factorial of given number

def fact(n):
    print(f"Computing Factorial of {n}")
    res = math.factorial(n)
    print(f"Factorial of {n} : {res}")
    return res


if __name__=="__main__":
    num = [5000,6000,700,8000]

    st = time.time()
    
    # pool of worker
    with multiprocessing.Pool() as pool:
        res = pool.map(fact,num)

    et = time.time()
    print(f"Result:{res}")
    print(f"Time Taken : {et-st} sec")
