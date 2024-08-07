# Problem: 2 Keys Keyboard - https://leetcode.com/problems/2-keys-keyboard/description/

class Solution:
    def minSteps(self, n: int) -> int:
        dp = [inf]*(n+2)
        dp[1] = 0

        for i in range(2, n+1):
            for j in range(1, i//2+1):
                if (i - j) % j == 0:
                    dp[i] = min(dp[i], dp[j]+(i-j)//j+1)
                    
        return dp[n]
