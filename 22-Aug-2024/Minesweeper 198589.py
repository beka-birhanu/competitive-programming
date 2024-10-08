# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board

        m , n = len(board), len(board[0])
        stack = [click]
        DIRECTIONS = [(1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1),(1,1),(-1,-1)]
        while stack:
            r, c = stack.pop()
            neibMine = []
            count = 0
            for dr, dc in DIRECTIONS:
                R = r + dr
                C = c + dc
                if 0 <= R < m and 0 <= C < n:
                    if board[R][C] == "E":
                        neibMine.append((R,C))
                    elif board[R][C] == "M":
                        count += 1
            if not count:
                stack.extend(neibMine)
                board[r][c] = "B"
            else:
                board[r][c] = str(count)
        return board

                