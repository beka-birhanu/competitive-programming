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
    #O(nlog(n))
    def minSubArrayLen_binarySearch(self, target, nums):
        n = len(nums)
        prefixSum = [0] * (n + 1)
        minLen = float("inf")

        for i in range(1, n + 1):
            prefixSum[i] = prefixSum[i - 1] + nums[i - 1]

        for i in range(n):
            left = i + 1
            right = n

            while left <= right:
                mid = left + (right - left) // 2
                sum = prefixSum[mid] - prefixSum[i]

                if sum >= target:
                    minLen = min(minLen, mid - i)
                    right = mid - 1
                else:
                    left = mid + 1

        return 0 if minLen == float("inf") else minLen
