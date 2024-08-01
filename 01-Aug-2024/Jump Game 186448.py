# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump =  1
        for idx, jump in enumerate(nums):
            max_jump -= 1
            max_jump = max(max_jump, jump)
            if max_jump <= 0:
                return idx == len(nums)-1
        
        return True