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

#time - O(n^2)
#space - O(n) + O(m)
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
            if row[i] or col[j]:
                mat[i][j] = 0

def setMatrixZeroOptimal(mat):
    n = len(mat)
    m = len(mat[0])
    col0 = 1

    # Step 1: Mark first row and first column as indicators
    for i in range(n):
        if mat[i][0] == 0:  # Check if any element in first column is 0
            col0 = 0
        
        for j in range(1, m):  # Start from second column
            if mat[i][j] == 0:
                mat[i][0] = 0  # Mark the row
                mat[0][j] = 0  # Mark the column

    # Step 2: Process the matrix (except first row and column)
    for i in range(1, n):
        for j in range(1, m):
            if mat[0][j] == 0 or mat[i][0] == 0:
                mat[i][j] = 0

    # Step 3: Process the first row
    if mat[0][0] == 0:
        for j in range(m):
            mat[0][j] = 0

    # Step 4: Process the first column
    if col0 == 0:
        for i in range(n):
            mat[i][0] = 0

# Reset the matrix
mat = [[1,1,1],[1,0,1],[1,1,1]]

# Call the optimal function and print the result
setMatrixZeroOptimal(mat)
print(mat)