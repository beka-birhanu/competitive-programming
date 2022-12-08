class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        maxSum = left = 0
        right = len(nums)-1
        nums.sort()
        while left < right:
            Sum = nums[left] + nums[right]
            maxSum = max(maxSum,Sum)
            left += 1
            right -= 1
        return maxSum
