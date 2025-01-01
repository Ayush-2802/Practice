str = 'chole bhature and lassi'
print("Original string:", str)
print("Replaced string:", str.replace("and", "&"))
print("Replaced string with max replacement:", str.replace("a", "A", 2)) # replaces first 2 'a's with 'A's
print("Replaced string with max replacement:", str.replace("a", "A", -2)) # replaces all 'a's with 'A's
print("Replaced string with max replacement:", str.replace("a", "A", 0)) # no replacement
print("Replaced string with max replacement:", str.replace("a", "A", 1)) # replaces first 'a' with 'A'
print("Replaced string with max replacement:", str.replace("a", "A", len(str))) # replaces all 'a's with 'A's