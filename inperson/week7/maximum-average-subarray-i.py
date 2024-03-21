class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = 0
        i = 0
        for j in range(k):
            curr_sum += nums[j]

        max_sum = curr_sum

        for j in range(k,len(nums)):
            curr_sum += nums[j]
            curr_sum -= nums[i]
            i += 1
            max_sum = max(max_sum, curr_sum)
        return max_sum/k