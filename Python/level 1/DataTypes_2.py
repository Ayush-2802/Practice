# Write a program that checks if a number is a positive, negative, or zero.

n = int(input("Enter a number to check (positive,negative,zero): "))

if n > 0 :
    print("The number is positive")
elif n < 0 :
    print("The number is negative")
else:   
    print("The number is zero")