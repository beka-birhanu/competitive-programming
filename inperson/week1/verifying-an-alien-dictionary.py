class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def check(word1,word2):
            
            for i in range(min(len(word1),len(word2))):
                if d[word1[i]] > d[word2[i]]:
                    
                    return False
                elif d[word1[i]] != d[word2[i]]:
                    return True

            return False if max(len(word1),len(word2)) != len(word2) else True
            

        d = {s:idx for idx,s in enumerate(order)}
        for i in range(len(words)-1):
            if not check(words[i],words[i+1]):
                return False
        return True