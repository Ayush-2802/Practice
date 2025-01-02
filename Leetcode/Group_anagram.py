from collections import defaultdict
def Group_anagram(strs):
    res = defaultdict(list)
    
    for i in strs:
        count = [0] * 26
        for s in i:
            count[ord(s) - ord("a")]+=1
        res[tuple(count)].append(i)
    return res.values()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Group_anagram(strs))