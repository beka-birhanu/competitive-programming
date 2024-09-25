# Problem: Check If Two String Arrays are Equivalent - https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        pointer1 = Pointer(word1)
        pointer2 = Pointer(word2)

        while pointer1.inbound() and pointer2.inbound():
            if pointer1.curr_letter() != pointer2.curr_letter():
                break
            
            pointer1.increment()
            pointer2.increment()
        
        matched_all = not(pointer1.inbound() or pointer2.inbound())
        return matched_all
        

class Pointer:
    def __init__(self, words):
        self.words = words
        self.pos = [0, 0]
    
    def increment(self):
        if self.pos[1] == len(self.words[self.pos[0]])-1:
            self.pos[0]+=1
            self.pos[1] = 0
        else:
            self.pos[1] += 1
    
    def inbound(self):
        return self.pos[0] < len(self.words)
    
    def curr_letter(self):
        return self.words[self.pos[0]][self.pos[1]]
