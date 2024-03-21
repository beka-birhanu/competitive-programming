class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        def mod_pow(num, _pow, mod):
            if _pow == 1:
                return num
            if _pow == 0:
                return 1
            if not _pow % 2:
                return (mod_pow(num, _pow//2, mod) ** 2) % mod

            return (num * mod_pow(num, _pow-1, mod) )% mod

        return (mod_pow(5, ceil(n/2), MOD)  * mod_pow(4,(n//2), MOD)) % MOD