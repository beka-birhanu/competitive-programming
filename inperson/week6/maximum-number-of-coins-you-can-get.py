class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        me = 0
        for i in range(len(piles)//3,len(piles),2):
            me += piles[i]
        return me