from math import log
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        power = round(log(n,3))
        return (3** power) == n
    def isPowerOfThree_recursive(self, n: int) -> bool:
        if n == 3 or n == 1:
            return True
        if n < 3 or n % 3 != 0:
            return False
        return self.isPowerOfThree_recursive(n//3)
