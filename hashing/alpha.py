arr = list(input("Enter string elements separated by space: ").split())
target = input("Enter the character to find its occurrence: ")

hash = [0] * 26
for word in arr:
        hash[ord(word.lower()) - ord('a')] += 1

print(f"'{target}' occurred: {hash[ord(target.lower()) - ord('a')]} times")