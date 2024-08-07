# Problem: Reach a Number - https://leetcode.com/problems/reach-a-number/

class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        l, r = 0, target
        while l < r:
            mid = (l+r)//2

            if arth_sum(mid) < target:
                l = mid+1
            else:
                r = mid

        steps = r
        while (arth_sum(steps) - target) % 2 != 0:
            steps += 1
        
        return steps

def arth_sum(n):
    return (n/2)*(n+1)