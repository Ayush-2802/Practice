str = 'CholeBhature,Lassi,Samosa,Kachori'
print("Original string:", str)
print("Split string:", str.split(",")) # splits string at ','

# More splitting examples
str2 = "Welcome to Python Programming"
print("Split by space:", str2.split())  # splits by whitespace
print("Split by 't':", str2.split('t'))  # splits at letter 't'
print("Split max 2 times:", str2.split(' ', 1))  # limits splits to 2

# Using splitlines
text = "Line1\nLine2\nLine3"
print("Split lines:", text.splitlines())  # splits at line breaks