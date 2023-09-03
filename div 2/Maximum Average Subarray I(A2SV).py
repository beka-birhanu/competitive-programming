class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        j = i + k-1
        max_sum =sum_ = sum(nums[i:j+1])

        for _ in range(k,len(nums)):
            j += 1
            sum_ = sum_ - nums[i] + nums[j]
            i += 1
            max_sum = max(sum_,max_sum)

        return max_sum/k
