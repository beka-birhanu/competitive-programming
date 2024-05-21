# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        power_set = []

        for i in range(2**n):
            subset = []
            idx = 0
            while i > 0:
                if i & 1 == 1:
                    subset.append(nums[idx])

                i >>= 1
                idx += 1

            power_set.append(subset)
        
        return power_set