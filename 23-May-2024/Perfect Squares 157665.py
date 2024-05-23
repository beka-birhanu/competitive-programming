# Problem: Perfect Squares - https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
		# step 1
        dp = [i for i in range(n+1)]
        
		# step 2
        for i in range(n+1):
	        j = 1
	        while j*j <= i:
	            dp[i] = min(dp[i], dp[i-(j*j)] + 1)
	            j += 1
        
        return dp[-1]