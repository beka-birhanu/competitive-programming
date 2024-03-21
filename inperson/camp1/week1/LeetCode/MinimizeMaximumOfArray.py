class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        curr_max = nums[0]
        running_sum = nums[0]

        for i in range(1,len(nums)):
            running_sum += nums[i]
            curr_max = max(curr_max,ceil(running_sum/(i+1)))

        return curr_max