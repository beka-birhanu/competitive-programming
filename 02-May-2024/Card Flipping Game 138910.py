# Problem: Card Flipping Game - https://leetcode.com/problems/card-flipping-game/description/

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        # stores nums in front and back of same cxard
        dic = set(val for idx,val in enumerate(fronts) if val == backs[idx])
        
        
        goods = list(i for i in set(fronts+backs) if i not in dic)
        return min(goods) if len(goods) else 0
        