# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        longest = s[0]

        for i in range(N):
            j = 1
            while j < min(i+1, N-i):
                if s[i-j] != s[i+j]:
                    break
                j += 1

            if j * 2 - 1 > len(longest):
                longest = s[i-j+1: i+j]
            
            j = 1
            while j < min(i+2, N-i):
                if s[i-j+1] != s[i+j]:
                    break
                
                j += 1

            if j * 2 -2 > len(longest):
                longest = s[i-j+2: i+j]

        return longest