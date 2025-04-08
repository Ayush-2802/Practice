def minimumOperations(num):
    seen = set()

    for i in range(len(num)-1,-1,-1):
        if num[i] in seen:
            return i // 3+1
        seen.add(num[i])
    return 0