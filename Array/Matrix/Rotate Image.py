def RotateImage(mat):
    n = len(mat)
    # Transpose the matrix (swap rows with columns)
    for i in range(n):
        for j in range(i+1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]  # Fixed the syntax error here
     
    for i in mat:
        i.reverse()
    
    return mat

# Test the function
if __name__ == "__main__":
    # Example matrix
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    RotateImage(matrix)
    
    print("\nRotated Image")
    for row in matrix:
        print(row)