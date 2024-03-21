class Solution:
    def minSubArrayLen(self, target, nums):

        minLen = float("inf")
        sum_ = 0
        i = 0

        for j in range(len(nums)):
            sum_ += nums[j]
            while sum_ >= target:
                minLen = min(minLen,j-i+1)
                sum_ -= nums[i]
                i += 1

                

        return 0 if minLen == float("inf") else minLen
