# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        masks = []
        for word in words:
            mask = 0
            for letter in word:
                mask |= 1 << (ord(letter) - ord('a'))
            
            masks.append(mask)

        max_value = 0
        for i in range(n):
            word1_length = len(words[i])
            mask1 = masks[i]
            for j in range(i+1, n):
                word2_length = len(words[j])
                mask2 = masks[j]

                have_common_letter = (mask1 & mask2) > 0
                if not have_common_letter:
                    max_value = max(max_value, word1_length * word2_length)
        
        return max_value
