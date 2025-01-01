password = input("Enter a password: ")
l = len(password)

if l>10:
    print("Password is strong")
elif l>6:
    print("Password is medium")
else:
    print("Password is weak")