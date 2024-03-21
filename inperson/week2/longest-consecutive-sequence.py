class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        _max = 0
        for i in nums:
            if not i-1 in nums:
                cur = i + 1
                while cur in nums:
                    cur += 1
            
                _max = max(_max,cur-i)


        return _max