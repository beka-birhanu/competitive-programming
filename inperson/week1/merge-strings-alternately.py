class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        for i in range(min(len(word1),len(word2))):
            ans += word1[i] + word2[i] 
        if len(word1) > len(word2):
            return ans + word1[len(word2):]
        else:
            return ans + word2[len(word1):]
  