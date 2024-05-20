# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0]*n
        dp[-1] = questions[-1][0]

        for i in range(n-2, -1, -1):
            skip_to = i+questions[i][1]+1
            points = questions[i][0]
            dp[i] = max(dp[i+1], points + (dp[skip_to] if skip_to < n else 0 ))

        return dp[0]