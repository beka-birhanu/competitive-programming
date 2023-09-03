from math import log
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        power = round(log(n,4))
        return (4** power) == n
