# Runtime 621ms and Memory 30.40MB

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_prefsum = nums[0]
        min_prefsum =  0
        max_prefsum = nums[0]
        for i in range(1,len(nums)):
            min_prefsum = min(cur_prefsum,min_prefsum)
            cur_prefsum += nums[i]
            max_prefsum = max(cur_prefsum-min_prefsum, max_prefsum)
        return max_prefsum
