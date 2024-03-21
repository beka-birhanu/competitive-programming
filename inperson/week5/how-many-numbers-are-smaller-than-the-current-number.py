class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        sorted_idx = {}
        
        ans = [0] * len(nums)
        for i in range(len(nums)):
            num = sorted_nums[i]

            if not num in sorted_idx:
                sorted_idx[num] = i  
        
        for i,el in enumerate(nums):
            ans[i] = sorted_idx[el] 
        
        return ans