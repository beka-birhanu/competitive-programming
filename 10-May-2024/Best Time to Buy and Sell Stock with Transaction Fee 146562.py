# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        @lru_cache(None)
        def dp(i: int, holding: int):
            if i == n:
                return 0
            do_nothing = dp(i+1, holding)
            do_something = 0
            if holding:
                # sell stock
                do_something = prices[i]-fee + dp(i+1, 0)
            else:
                # buy stock
                do_something = -prices[i] + dp(i+1, 1)

            return max(do_nothing, do_something)

        return dp(0, 0)
        