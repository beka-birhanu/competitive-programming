class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = len(s)-1
        ans = ""
        while i >= 0:
            if s[i] == "#":
                ans = chr(int(s[i-2:i])+96) + ans
                i -= 2

            else:
                ans = chr(int(s[i])+96) + ans
            i -= 1
        return ans
