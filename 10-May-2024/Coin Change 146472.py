# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(amt):
            if amount == amt:
                return 0
            
            if amount < amt:
                return inf
            
            if amt not in memo:
                memo[amt] = min(1+ dp(amt + coin)for coin in coins)
            
            return memo[amt]
        
        _min =  dp(0) 
        return _min if _min < inf else -1
