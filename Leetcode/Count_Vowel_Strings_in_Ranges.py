def solution(words,queries):
    def vowel(c):
        return c in "aeiou"

    res = []
    p = []
    count = 0

    for i in words:
        if vowel(i[0]) and vowel(i[-1]):
            count += 1
        p.append(count)

    for j in queries:
        (l,r) = j
        if l == 0:
            res.append(p[r])
        else:
            res.append(p[r] - p[l-1])
        
    return res


words = ["aba","bcb","ece","aa","e"]
queries = [[0,2],[1,4],[1,1]]

print(solution(words,queries))