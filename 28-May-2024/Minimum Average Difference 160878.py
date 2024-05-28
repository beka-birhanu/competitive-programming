# Problem: Minimum Average Difference - https://leetcode.com/problems/minimum-average-difference/

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [nums[0]]*n
        
        for i in range(1, n):
            pre[i] = pre[i-1]+nums[i]
        
        res, ans = float("inf"), 0
        for i in range(n):
            n1 = pre[i] // (i+1)
            n2 = 0 if i==n-1 else (pre[-1]-pre[i]) // (n-i-1)
            val = abs(n1-n2)
            if val < res:
                res = val
                ans = i
        
        return ans