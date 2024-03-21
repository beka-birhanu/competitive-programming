class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        _max = max(candies)
        for i in range(len(candies)):
            candies[i]  = _max <= candies[i]+extraCandies
        return candies   