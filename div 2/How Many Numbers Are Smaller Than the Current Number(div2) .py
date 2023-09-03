class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        num_sorted = sorted(nums)
        for i in range(n):
            ans[i] = num_sorted.index(nums[i])
        return ans
