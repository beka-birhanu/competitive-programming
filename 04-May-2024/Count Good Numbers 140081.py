# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
       
        return (pow(5, ceil(n/2), MOD)  * pow(4,(n//2), MOD)) % MOD