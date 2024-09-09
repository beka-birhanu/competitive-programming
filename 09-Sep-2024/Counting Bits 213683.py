# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> list[int]:
        bits = [0] * (n + 1)
        for x in range(n + 1):
            bits[x] = bits[x // 2] + (x % 2)
            
        return bits
