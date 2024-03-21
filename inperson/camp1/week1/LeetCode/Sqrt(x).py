class Solution:
    def mySqrt(self, x: int) -> int:

        i,j = 0,x//2 + 1
        while i <= j:
            m = (i + j)//2
            if m**2 <= x < (m+1)**2:
                return m
            if m**2 > x:
                j = m-1
            else:
                i = m+1