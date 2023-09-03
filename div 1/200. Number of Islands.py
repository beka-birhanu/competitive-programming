class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        def search(i, j):
            q = deque()
            q.append((i, j))
            while q:
                currRow, currCol = q.popleft()
                for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    r = currRow + dr
                    c = currCol + dc
                    if 0 <= r < row and 0 <= c < col and grid[r][c] == '1':
                        grid[r][c] = '-1'
                        q.append((r, c))
            
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    search(i, j)
                    count += 1
        
        return count
