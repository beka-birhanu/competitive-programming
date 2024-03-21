class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(max_weight,days):
            d_weight = 0
            for w in weights:
                d_weight += w
                if d_weight > max_weight:
                    days -= 1
                    d_weight = w
            return days > 0

        maxim = sum(weights)
        minim = max(weights)

        while maxim > minim:
            mid = (maxim+minim)//2
            if check(mid,days):
                maxim = mid
            else:
                minim = mid + 1

        return maxim