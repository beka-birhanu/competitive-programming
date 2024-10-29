# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = bisect.bisect(matrix, [target, inf])
        if row == 0: 
            return False
    
        col = bisect.bisect(matrix[row-1], target)
        return matrix[row-1][col-1] == target