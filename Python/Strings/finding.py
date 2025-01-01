str = 'CholeBhature,Lassi,Samosa,Kachori'
print("Original string:", str)
print("Find 'Samosa':", str.find("Samosa"))  # finds 'Samosa' in string

# More finding examples
print("Find 'Dosa':", str.find("Dosa"))  # returns -1 if not found
print("Find 'Samosa' from index 10:", str.find("Samosa", 10))  # finds 'Samosa' from index 10
print("Find 'Samosa' in 0 to 10:", str.find("Samosa", 0, 10))  # finds 'Samosa' in 0 to 10

# Using rfind
print("Find 'Samosa':", str.rfind("Samosa"))  # finds 'Samosa' from right
print("Find 'Dosa':", str.rfind("Dosa"))  # returns -1 if not found

# Using index
print("Find 'Samosa':", str.index("Samosa"))  # finds 'Samosa' in string

# Using rindex
print("Find 'Samosa':", str.rindex("Samosa"))  # finds 'Samosa' from right
print("Find 'Dosa':", str.rindex("Dosa"))  # returns -1 if not found
