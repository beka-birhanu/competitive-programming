# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        i = 0

        while i < len(nums):
            if nums[i] == i + 1:
                i += 1 
                continue

            if 0 < nums[i] <= N and nums[i] != nums[nums[i]-1]:
                temp = nums[i]-1
                nums[i] = nums[nums[i]-1]
                nums[temp] = temp+1
                continue
            
            i += 1

        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1
            
        return N + 1
            
        