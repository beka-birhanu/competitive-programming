class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows_max = [0]*n
        cols_max = [0]*n
        for i in range(n):
            row_max = 0
            for j in range(n):
                row_max = max(row_max, grid[i][j])
                cols_max[j] = max(cols_max[j], grid[i][j])
            
            rows_max[i] = row_max

        max_increase = 0
        for i in range(n):
            for j in range(n):
                max_increase += min(rows_max[i],cols_max[j]) - grid[i][j]
            
        return max_increase