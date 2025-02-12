# Convert palindrome checker to lambda
check_palindrome = lambda num: num == num[::-1]
num = input("Enter the number :")
print(check_palindrome(num))