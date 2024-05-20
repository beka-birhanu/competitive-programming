# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        dp = defaultdict(int)
        dp[arr[-1]] = 1

        for i in range(n-2, -1, -1):
            pick = 1 + dp[arr[i]+difference]
            dp[arr[i]] = max(dp[arr[i]], pick)

        return max(dp.values())