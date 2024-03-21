class Solution:
    def totalMoney(self, n: int) -> int:
        n, r =divmod(n,7)
        return int(n/2*(56 + (n-1)*7) + ( r/2)*(2*n+r+1))