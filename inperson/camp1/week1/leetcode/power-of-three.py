class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n <= 1:
            return n == 1
        if n%3:
            return False
        
        return self.isPowerOfThree(n//3)