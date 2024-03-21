class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        # stores numbers maped to a boolean that states wheter it is good number in or not 
        dic = defaultdict(lambda : True)
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                dic[fronts[i]] = False
        
        goods = list(i for i in set(fronts+backs) if dic[i])
        return min(goods) if len(goods) else 0
        