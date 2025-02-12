# Convert palindrome checker to lambda
check_palindrome = lambda num: num == num[::-1]

# Get input and print result
if __name__ == "__main__":
    num = input("Enter the number :")
    print(check_palindrome(num))