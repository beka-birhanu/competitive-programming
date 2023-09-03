class Solution:
#     def maxCoins(self, piles: List[int]) -> int:
#         piles.sort()
#         max_coin = left = 0
#         right = len(piles)-1

#         while left < (right-1):
#             max_coin += piles[right-1]
#             left +=1
#             right -= 2
#         return max_coin
#



# no need to iterate with two pointers
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        me = 0
        for i in range(n//3,n,2):
            me += piles[i]
        return me
