# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False

                i+= 1
                j-= 1

            return True

        n = len(s)
        dp = [[] for _ in range(n+1)]
        dp[-1].append([])

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if is_palindrome(i, j):
                    next_results = dp[j+1]

                    for next_result in next_results:
                        dp[i].append([s[i:j+1]]+ next_result)
        
        return dp[0]