# Problem: Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        n=len(s)
        dp=[n]*(n+1)
        dp[n] = -1

        for i in range(n-1,-1,-1):
            temp=''
            for j in range(i,n):
                temp += s[j]
                if temp == temp[-1::-1]:
                    dp[i]=min(dp[i], 1+dp[j+1])

        return dp[0]