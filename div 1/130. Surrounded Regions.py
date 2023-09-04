# Runtime 129ms and Memory 17.5 mb
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def mark(i,j):
            stack = [(i,j)]
            while stack:
                i,j = stack.pop()
                for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                    cI = i + dx
                    cJ = j + dy
                    if 0 <= cI < m and 0 <= cJ < n and board[cI][cJ] == "O" and (cI,cJ) not in unsurrounded:
                        unsurrounded.add((cI,cJ))
                        stack.append((cI,cJ))
        m, n = len(board),len(board[0])
        unsurrounded = set()

        for i in [0,m-1]:
            for j in range(n):
                if board[i][j] == "O":
                    mark(i,j)
        for i in range(m):
            for j in [0,n-1]:
                if board[i][j] == "O":
                    mark(i,j)
        for i in range(1,m-1):
            for j in range(1,n-1):
                if (i,j) not in unsurrounded and board[i][j] == "O":
                    board[i][j] = "X"
                
