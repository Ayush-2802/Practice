def matadd(mat1,mat2):
    n = len(mat1)
    m = len(mat1[0])
    res = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            res[i][j] = mat1[i][j] + mat2[i][j] 
    return res


mat1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
mat2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

res = matadd(mat1,mat2)
print(res)