# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        heapify(costs)
        total_icecream = 0

        while costs and costs[0] <= coins:
            coins -= heappop(costs)
            total_icecream += 1
        
        return total_icecream