# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = triangle[-1]

        for i in range(n-2, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j+1], dp[j]) + triangle[i][j]
        
        return dp[0]