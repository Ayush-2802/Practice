# Write a program that takes a string input from the user and prints it in reverse order.

str = input("Enter a string: ")
print(str[::-1])


# Write a program that takes a string input from the user and counts the number of vowels in the string.
v = ['a', 'e', 'i', 'o', 'u']
count = 0
str = input("Enter a string: ")
for i in str:
    if i in v:
        count+=1
print(count)

# Create a program that checks if a word is a palindrome (reads the same forwards and backwards).
str = input("Enter a string: ")
strrev = str[::-1]
if str == strrev:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")