#optimal
def lengthOfLastWord(s):
    w = s.split()
    return len(w[-1])

#my brute approach
def lengthOfLastWord(s):
    # brute
    m = 0
    c = 0
    for i in s:
        if i.isalpha():
            c += 1
            m = c
        elif i == " ":
            c = 0
    return m