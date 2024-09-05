# Problem: Number of Smooth Descent Periods of a Stock - https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        prices.append(inf) # To help count the last sequence
        ans = 0
        i = 0
        for j in range(1, len(prices)):
            if prices[j] == prices[j-1] - 1:
                continue
            n = j-i
            ans += n*(n+1)/2
            i = j
        
        return int(ans)
