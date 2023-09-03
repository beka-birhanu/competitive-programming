class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i,j):
            stack = [(i,j)]
            count = 0
            while stack:
                i,j = stack.pop()
                count += 1
                for dx, dy in [(0,1),(0,-1),(-1,0),(1,0)]:
                    cI = i + dx
                    cJ = j + dy
                    if 0 <= cI < m and 0 <= cJ < n and grid[cI][cJ]:
                        grid[cI][cJ] = 0
                        stack.append((cI,cJ))
                        
            return count
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    grid[i][j] = 0
                    max_area = max(max_area, dfs(i,j))
        return max_area
