# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        far_prev = 0
        near_prev = nums[-1]
        curr = near_prev

        for i in range(n-2, -1, -1):
            curr = max(far_prev+nums[i], near_prev)
            far_prev = near_prev
            near_prev = curr
        
        return curr