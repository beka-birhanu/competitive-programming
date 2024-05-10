# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def dp(i, curr_sum):
            if curr_sum == target and i == len(nums):
                return 1
            
            if i == len(nums):
                return 0
            
            if (i, curr_sum) not in memo:
                memo[(i, curr_sum)] = dp(i+1, curr_sum+nums[i]) + dp(i+1, curr_sum-nums[i])
            
            return memo[(i, curr_sum)]
        
        return dp(0, 0)

