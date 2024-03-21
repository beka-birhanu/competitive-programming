class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)

        pre_sum = 0
        for i in range(len(nums)):
            if pre_sum == total_sum - (nums[i]+pre_sum):
                return i
            pre_sum += nums[i]
            
        return -1