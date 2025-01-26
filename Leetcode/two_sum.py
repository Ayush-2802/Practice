class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = list()
        for i in range(1,numRows+1):
            currentRow = [1]*i    

            for j in range(1, i-1):
                currentRow[j] = res[i-2][j-1] + res[i-2][j]
                
            res.append(currentRow)
        return res
            