# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 or n <= 1:
            return x ** n
            
        if n < 0:
            return 1/self.myPow(x,-n)

        if n % 2:
            return x * self.myPow(x,n-1)
            
        else:
            return self.myPow(x*x,n//2)