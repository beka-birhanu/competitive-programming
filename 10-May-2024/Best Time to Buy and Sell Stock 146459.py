# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currProfit, maxProfit = 0, 0      
        for i in range(1, len(prices)):
            currTick = prices[i] - prices[i-1]
            currProfit = max(currTick, currTick + currProfit)
            maxProfit = max(currProfit, maxProfit)
        return maxProfit