class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[0]*(len(matrix[0])+1) for i in range(len(matrix)+1)]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.prefix[r+1][c+1] = self.prefix[r][c+1] + self.prefix[r+1][c] - self.prefix[r][c] + matrix[r][c] 

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix[row2+1][col2+1] - self.prefix[row2+1][col1] - self.prefix[row1][col2+1] + self.prefix[row1][col1]
        
class NumMatrix2:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for r in matrix:
            for i in range(1,len(r)):
                r[i] += r[i-1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1,row2+1):
            ans += self.matrix[i][col2] - self.matrix[i][col1-1] if col1 else self.matrix[i][col2]

        return ans 
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
