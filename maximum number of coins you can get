class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        max_coin = left = 0
        right = len(piles)-1

        while left < (right-1):
            max_coin += piles[right-1]
            left +=1
            right -= 2
        return max_coin
