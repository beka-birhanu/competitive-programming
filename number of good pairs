class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] == nums[right]:
                count += 1
            right -= 1

            if left == right:
                left += 1
                right = len(nums) - 1

        return count
