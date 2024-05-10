# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @lru_cache(None)
        def dp(i: int, holding: int):
            if i >= n:
                return 0
            do_nothing = dp(i+1, holding)
            do_something = 0
            if holding:
                # sell stock
                do_something = prices[i] + dp(i+2, 0)
            else:
                # buy stock
                do_something = -prices[i] + dp(i+1, 1)

            return max(do_nothing, do_something)

        return dp(0, 0)