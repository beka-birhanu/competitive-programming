# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class WordDictionary:

    def __init__(self):
        self.root = {'$': False}
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for letter in word:
            if letter not in curr:
                curr[letter] = {'$': False}
            
            curr = curr[letter]
        
        curr['$'] = True

    def search(self, word: str) -> bool:
        def helper(i, word, curr):
            if i >= len(word):
                return curr['$']
            
            curr_letter = word[i]

            if curr_letter in curr:
                return helper(i+1, word, curr[curr_letter])

            if curr_letter != '.' and curr_letter not in curr:
                return False
            
            for val, childs in curr.items():
                if val != '$' and helper(i+1, word, childs):
                    return True
                
            return False

        return helper(0, word, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

