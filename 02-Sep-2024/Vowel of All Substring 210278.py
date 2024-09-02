# Problem: Vowel of All Substring - https://leetcode.com/problems/vowels-of-all-substrings/

class Solution:
    def countVowels(self, word: str) -> int:
        vowels = "aeiou"
        count = 0
        for i, letter in enumerate(word):
            if letter in vowels:
                count += (len(word)-i) * (i+1)
        
        return count