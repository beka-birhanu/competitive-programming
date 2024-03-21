class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        prev = self.kthGrammar(n-1, ceil(k/2))
        if prev == 1:
            if k % 2:
                return 1
            
            else:
                return 0
        else:
            if k % 2:
                return 0
            
            else:
                return 1
        