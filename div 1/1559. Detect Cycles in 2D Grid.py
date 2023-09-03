class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        def dfs(i,j):
            stack = [(i,j,0,0)]
            while stack:
                r, c, pr, pc = stack.pop()
                for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    cR = r + dx
                    cC = c + dy
                    if 0 <= cR < m and 0 <= cC < n  and (cR,cC) != (pr,pc) and grid[cR][cC].upper() == grid[i][j].upper():
                        if grid[cR][cC].isupper():
                            return True
                        else:
                            grid[cR][cC] = grid[cR][cC].upper()
                            stack.append((cR,cC,r,c))
            return False
        for i in range(m):
            for j in range(n):
                if grid[i][j].islower():
                    grid[i][j] = grid[i][j].upper()
                    if dfs(i,j):
                        return True
        return False
