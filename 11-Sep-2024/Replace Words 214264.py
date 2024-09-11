# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = {'$': False}
        
        for word in dictionary:
            curr = root
            for letter in word:
                if letter not in curr:
                    curr[letter] = {'$': False}

                curr = curr[letter]
                if curr['$']:
                    break
            
            curr['$'] = True
        
        replaced_words = []

        for word in sentence.split():
            curr = root
            replaced_word = word
            
            for i, letter in enumerate(word):
                if curr['$']:
                    replaced_word = word[:i]
                    break

                if letter not in curr:
                    break
                
                curr = curr[letter]
            
            replaced_words.append(replaced_word)

        return " ".join(replaced_words)