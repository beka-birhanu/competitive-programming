# Problem: Car fleet - https://leetcode.com/problems/car-fleet/

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        initials = sorted(list(zip(position,speed)),reverse=True) 
        latest = 0
        fleets = 0
        for pos, vel in initials:
            t = (target-pos)/vel
            if t > latest:
                fleets += 1
                latest = t

        return fleets