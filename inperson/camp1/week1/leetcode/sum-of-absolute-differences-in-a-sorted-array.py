class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        
        pref_sum = 0
        for i in range(len(nums)):
            pref_sum += nums[i]
            nums[i] = ((total_sum - pref_sum) - nums[i]*(len(nums)-i-1)) +  (nums[i]*(i+1))- pref_sum
            

        return nums