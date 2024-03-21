class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        for shop in range(len(costs)):
            coins -= costs[shop]
            if coins < 0:
                return shop
        return len(costs)