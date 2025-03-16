def longestCommonPrefix(strs):
    strs = sorted(strs)
    n = len(strs)
    f = strs[0]
    l = strs[n-1]
    res = ""
    if n <=1:
        return f
    else:
        for i in range(len(f)):
            if f[i] != l[i]:
                break
            res += f[i]
    return res