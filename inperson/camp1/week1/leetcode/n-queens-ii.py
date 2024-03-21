class Solution:
    def totalNQueens(self, n: int) -> int:
        def solve(row):
            nonlocal solutions
            if row == n:
                solutions += 1

            for i in range(n):
                if (i not in is_at_col) and (row + i not in is_at_d1) and (i - row not in is_at_d2):
                    is_at_col.add(i)
                    is_at_d1.add(row+i)
                    is_at_d2.add(i-row)

                    solve(row+1)

                    is_at_col.remove(i)
                    is_at_d1.remove(row+i)
                    is_at_d2.remove(i-row)

        solutions = 0

        is_at_col = set()
        is_at_d1 = set()
        is_at_d2 = set()
        
        solve(0)

        return solutions