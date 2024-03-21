class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_sum =  0
        max_sum = -inf
        pref_sum = 0
        for num in nums:
            pref_sum += num
            max_sum = max(max_sum, pref_sum - min_sum)
            min_sum = min(min_sum, pref_sum)
        return max_sum