class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        max_dist = 0
        for house in houses:
            pos = bisect.bisect(heaters, house)
            curr_radi = (house - heaters[pos-1] )if pos > 0 else inf
            
            if pos < len(heaters):
                curr_radi = min(curr_radi, heaters[pos] - house)
            
            max_dist = max(max_dist, curr_radi)
            
        return max_dist