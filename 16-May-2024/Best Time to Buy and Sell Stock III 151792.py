# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        pre_max_profit = [0]*N  #maximum profit that can be yeild if bought and sold BEFORE today and including today
        pst_max_profit = [0]*N  #maxumum profit that can be yeild if bought and sold AFTER today
        
        curr_min_price = prices[0]
        for i in range(1, N):
            curr_price = prices[i]
            pre_max_profit[i] = max(pre_max_profit[i-1], (curr_price - curr_min_price))
            curr_min_price = min(curr_min_price, curr_price)
        
        curr_max_price = prices[N-1]
        if_bought_after_today = 0
        for i in range(N-2, -1, -1):
            curr_price = prices[i]
            pst_max_profit[i] = max(if_bought_after_today, pst_max_profit[i+1])
            if_bought_after_today = curr_max_price - curr_price
            curr_max_price = max(curr_price, curr_max_price)
        
        # sum up the two lists to find maximum profit if bought and sold until today and after today
        # then return the maximum
        max_profit = 0
        for i in range(N):
            curr_profit = pre_max_profit[i] + pst_max_profit[i]
            max_profit = max(curr_profit, max_profit)
        
        return max_profit