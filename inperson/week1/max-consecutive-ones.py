class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        _max = 0
        i = 0
        while i < len(nums):
            count = 0
            while i < len(nums) and nums[i] == 1:
                count += 1
                i += 1
            _max = max(_max,count)
            count = 0
            i += 1
        return _max