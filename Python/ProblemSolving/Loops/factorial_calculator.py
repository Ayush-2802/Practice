n = int(input("Enter a number: "))

if n<0:
    print("Factorial does not exist for negative numbers")
elif n==0:
    print("Factorial of 0 is 1")
else:
    fact = 1
    # for i in range(1,n+1):
    #     fact = fact*i
    # print("Factorial of",n,"is",fact)

    while n>0:
        fact = fact*n
        n -= 1
    print("Factorial is",fact)