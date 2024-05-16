# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[-inf, -inf] for _ in range(n+1)]
        dp[-1] = [0, 0]

        for i in range(m-1, -1, -1):

            for j in range(n-1, -1, -1):
                path1 = [dp[j][0] + dungeon[i][j], min(dungeon[i][j], dp[j][1] + dungeon[i][j], 0)]
                path2 = [dp[j+1][0] + dungeon[i][j], min(dungeon[i][j], dp[j+1][1] + dungeon[i][j], 0)]
                dp[j] = max(path1, path2, key = lambda x: x[::-1])

            dp[-1][0] = -inf
            dp[-1][1] = -inf

        return max(0 - dp[0][-1] + 1, 0)

