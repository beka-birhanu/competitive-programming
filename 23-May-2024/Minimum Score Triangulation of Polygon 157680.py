# Problem: Minimum Score Triangulation of Polygon - https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        N = len(values)
        dp = [[0]*N for _ in range(N)]
        
        for size in range(2, N):
            for left in range(N-size):
                right = left + size
                adj = values[left] * values[right]

                _min = inf
                for pivot in range(left+1, right):
                    _min = min(_min, adj*values[pivot] + dp[left][pivot] + dp[pivot][right])
                
                dp[left][right] = _min

        return dp[0][-1]