# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class Solution:
    def longestWord(self, words: List[str]) -> str:
        def insert(word, root):
            curr = root
            for letter in word[:-1]:
                if letter not in curr:
                    return False
                
                curr = curr[letter]
            
            if not curr['is_end']:
                return False
            
            if word[-1] not in curr:
                curr[word[-1]] = {'is_end': True}

            return True

        root = {'is_end': True}
        words.sort(key = lambda word: (len(word), word))
        longest = ''

        for word in words:
            if insert(word, root) and len(word) > len(longest):
                longest = word
        
        return longest