n = int(input("Enter a number: "))

# if n > 1:
#     #while loop to check if the number is prime or not
#     while n % 2 == 0:
#         print("Not a prime number")
#         break
#     else:
#         print("Prime number")
# else:
#     print("Not a prime number")
    
# for loop to check if the number is prime or not
if n > 1:
    for i in range(2,n):
        if (n % i) == 0:
            print("not a prime number")
            break
    else:
        print("prime number")
else:
    print("not a prime number")