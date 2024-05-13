# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache 
        def helper(i, j):
            if i >= n or j >= m:
                return 0
            
            exclude = helper(i+1, j)
            pos = -1
            for k in range(j , m):
                if text2[k] == text1[i]:
                    pos = k
                    break
            
            include = 0
            if pos >= 0:
                include = 1 + helper(i+1, pos+1)

            return max(include, exclude)
        
        n, m = len(text1), len(text2)
        return helper(0, 0)