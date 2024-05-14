# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def helper(row, col):
            if row == 1 or col == 1:
                return 1
            
            return helper(row-1, col) + helper(row, col-1)
        
        return helper(m, n)