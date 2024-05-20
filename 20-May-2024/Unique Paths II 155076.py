# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0]*(n+1)
        dp[-2] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[j] += dp[j+1]
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
        
        return dp[0]