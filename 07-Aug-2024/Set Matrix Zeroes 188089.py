# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        is_zero_row = [False]*m
        is_zero_col = [False]*n

        for i in range(m):
            for j in range(n):
                is_zero = matrix[i][j] == 0
                if is_zero:
                    is_zero_row[i] = is_zero
                    is_zero_col[j] = is_zero
                    
        for i in range(m):
            for j in range(n):
                is_zero = is_zero_row[i] | is_zero_col[j]
                if is_zero:
                    matrix[i][j] = 0
                