# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, CLOS = len(grid), len(grid[0])

        def dfs(i, j):
            if not (0 <= i < ROWS and 0 <= j < CLOS) or grid[i][j] != 1:
                return 0
            grid[i][j] = 0
            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)

        res = 0
        for i in range(ROWS):
            for j in range(CLOS):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
                    
        return res