class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def solve(row,col) -> bool:
            if row >= 9:
                return  True
            
            for i in range(col, 9):
                if board[row][i] != ".":
                    continue

                for val in ["5","3","4","6","7","8","9","1","2"]:
                    if val not in at_col[i] and val not in at_row[row] and val not in at_sub[(row//3,i//3)]:
                        # print(val,row,i,at_col,at_row, at_sub)
                        board[row][i] = val
                        at_col[i].add(val)
                        at_row[row].add(val)
                        at_sub[(row//3, i//3)].add(val)

                        if i < 8:
                            if solve(row, i+1):
                                return True
                        else:
                            if solve(row+1,0):
                                return True
                        
                        board[row][i] = "."
                        at_col[i].remove(val)
                        at_row[row].remove(val)
                        at_sub[(row//3, i//3)].remove(val)

                if board[row][i] == ".":
                    return False
                    
            return solve(row+1, 0)

        at_col = defaultdict(set)
        at_row = defaultdict(set)
        at_sub = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue

                at_col[col].add(board[row][col])
                at_row[row].add(board[row][col])
                at_sub[(row//3, col//3)].add(board[row][col])
        
        solve(0,0)