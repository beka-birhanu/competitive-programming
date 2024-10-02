# Problem: Broken Calculator - https://leetcode.com/problems/broken-calculator/description/

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        ops = 0

        while startValue < target:
            if target % 2:
                ops += 1 
                target += 1
            
            target //= 2
            ops += 1

        ops += startValue - target

        return ops      
