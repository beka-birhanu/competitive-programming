class Solution:
    def largestMerge(self, s1: str, s2: str) -> str:
        ans = ""
        while s1 and s2:
            if s1 > s2:
                ans += s1[0]
                s1 = s1[1:]
            else:
                ans += s2[0]
                s2 = s2[1:]
        return ans + s1 + s2

    # this next one will be easier to understand what needs to happen
    def largestMerge_2( self,word1: str, word2: str) -> str:
    
            def curr_best() -> None:
                nonlocal i,j,ans
                c = 0
                while ( i < len(word1) and j < len(word2)) and (word1[i] == word2[j]):
                    i += 1
                    j += 1
                    c += 1
                if (i == len(word1)) or ( i < len(word1) and j < len(word2)) and (word1[i] < word2[j]):
                    ans += word2[j-c]
                    j -= (c-1)
                    i -= c
    
                elif j == len(word2) or ( i < len(word1) and j < len(word2)) and (word1[i] > word2[j]):
                    ans += word1[i-c]
                    i -= (c-1)
                    j -= c
    
            i,j = 0,0
            ans = ""
    
            while i < len(word1) and j < len(word2):
                if word1[i] > word2[j]:
                    ans += word1[i]
                    i += 1
                elif word1[i] < word2[j]:
                    ans += word2[j]
                    j += 1
                else:
                    curr_best()
    
            if j < len(word2):
                ans += word2[j:]
    
            if i < len(word1):
                ans += word1[i:]
    
            return ans

