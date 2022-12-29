class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            return ''.join('1' if x == '0' else '0' for x in s)
        def generator(n):
            if n == 1:
                return '0'
            else:
                return generator(n-1) + "1" + invert(generator(n-1))[::-1]
        return generator(n)[k-1]
