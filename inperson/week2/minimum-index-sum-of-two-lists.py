class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list2 = {s:idx for idx,s in enumerate(list2)}
        
        # stores common string with index sum
        dic = defaultdict(lambda : -1)
        min_sum = inf
        for idx,s in enumerate(list1):
            if s in list2:
                dic[s] = idx+list2[s]
                min_sum = min(dic[s],min_sum)
        return [s for s,v in dic.items() if v == min_sum ]
