# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def helper(i, amount):
            if amount == 0:
                return 1
            
            if amount < 0:
                return 0
            
            possiblities = 0
            for j in range(i, len(coins)):
                coin = coins[j]
                possiblities += helper(j, amount - coin)
            
            return possiblities
        
        coins.sort(reverse = True)
        return helper(0, amount)