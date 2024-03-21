class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        
        sub = {(0,0):set(),(0,1):set(),(0,2):set(),(1,0):set(),(1,1):set(),(1,2):set(),(2,0):set(),(2,1):set(),(2,2):set()}

        for i in range(9):
            for j in range(9):
                x = board[i][j]
                if x != ".":
                    if x in row[i] or x in col[j] or x in sub[(i//3,j//3)]:
                        return False
                    row[i].add(x)
                    col[j].add(x)
                    sub[(i//3,j//3)].add(x)
        return True