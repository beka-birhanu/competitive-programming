class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumps_left = nums[0]
        for i in range(len(nums)):
            jumps_left -= 1
            jumps_left = max(jumps_left,nums[i])

            if not jumps_left and i < len(nums)-1:
                return False

        return True
