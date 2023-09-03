# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        if isBadVersion(1):
            return 1
        i,j = 1,n
        while i <= j:
            m = (i + j)//2
            if isBadVersion(m) and not isBadVersion(m-1):
                return m

            if isBadVersion(m-1):
                j = m-1
            else:
                i = m + 1
