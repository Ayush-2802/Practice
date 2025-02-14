arr = list(input("Enter string elements separated by space: ").split())

hash = {}

for word in arr:
    hash[word] = hash.get(word, 0) + 1

print(f"maximum frequency is {max(hash.values())} and the word is {max(hash, key=hash.get)}")
print(f"minimum frequency is {min(hash.values())} and the word is {min(hash,key=hash.get)}")