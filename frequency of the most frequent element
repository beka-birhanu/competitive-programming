class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        sliding_sum = max_freq = left = 0
        nums.sort()
        for right in range(len(nums)):
            sliding_sum += nums[right]

            while ((right - left + 1) * nums[right]) - sliding_sum > k:
                sliding_sum -= nums[left]
                left += 1

            max_freq = max(max_freq, (right - left + 1))

        return max_freq
