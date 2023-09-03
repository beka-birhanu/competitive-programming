from math import log
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        power = round(log(n,4))
        return (4** power) == n

    def isPowerOfFour_recursive(self, n: int) -> bool:
        if n == 4 or n == 1:
            return True
        if n < 4 or n % 4 != 0:
            return False
        return self.isPowerOfFour(n//4)
