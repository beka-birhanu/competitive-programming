class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels_cnt = 0
        for i in range(k):
            if s[i] in "aeiou":
                vowels_cnt += 1
        
        largest_cnt = vowels_cnt 

        for i in range(k,len(s)):
            if s[i] in "aeiou":
                vowels_cnt += 1

            if s[i-k] in "aeiou":
                vowels_cnt -= 1
            
            largest_cnt = max(vowels_cnt,largest_cnt)

        return largest_cnt