mat = [[1,1,1],[1,0,1],[1,1,1]]

#complexity O(n^3)
def setMatrixZeroBrute(mat):
    n = len(mat)
    m = len(mat[0])
    
    def markR(i,mat):
        for j in range(m):
            if mat[i][j] != 0:
                mat[i][j] = -1

    def markC(j,mat):
        for i in range(n):
            if mat[i][j] != 0:
                mat[i][j] = -1

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                markR(i, mat)
                markC(j, mat)
    
    for i in range(n):
        for j in range(m):
            if mat[i][j] == -1:
                mat[i][j] = 0


def setMatrixZeroBetter(mat):
    n = len(mat)
    m = len(mat[0])
    row = [0]*n
    col= [0]*m

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                row[i] = 1
                col[j] = 1
            
    for i in range(n):
        for j in range(m):
            if row[i] == 1 or col[j] == 1:
                mat[i][j] = 0
