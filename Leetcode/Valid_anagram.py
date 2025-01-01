def valid_anagram(s,t):
    if len(s)!=len(t):
        return False
    
    #method 1 
    return Counter(s) == Counter(t)

    #method 2 
    return sorted(s) == sorted(t)

    #method 3 
    count1 = [0]*26
    count2 = [0]*26
    for i in range(len(s)):
        count1[ord(s[i])-ord('a')]+=1
        count2[ord(t[i])-ord('a')]+=1
    return count1 == count2
