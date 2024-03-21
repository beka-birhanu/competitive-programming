class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        diagonal_starts = {}

        for i,val in enumerate(matrix[0]):
            diagonal_starts[i] = val

        for i in range(1,len(matrix)):
           diagonal_starts[-i] = matrix[i][0]
            
        
        for i in range(len(matrix)):
            for j in range(1, len(matrix[0])):
                    if matrix[i][j] != diagonal_starts[j-i]:
                        return False
        return True
       