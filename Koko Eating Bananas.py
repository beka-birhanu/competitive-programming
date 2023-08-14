class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(speed,h):
            for p in piles:
                h -= p // speed + 1 if p % speed else  p // speed
            return h >= 0
        maxSpeed = sum(piles)
        minSpeed = math.ceil( maxSpeed / h)

        while maxSpeed > minSpeed:
            mid =( maxSpeed + minSpeed)//2
            if possible(mid,h):
                maxSpeed = mid
            else:
                minSpeed = mid + 1
        return maxSpeed
