# Problem: Find Indices With Index and Value Difference I - https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/description/

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        no_answer = [-1, -1]
        if indexDifference >= len(nums):
            return no_answer
        
        max_idx = min_idx = 0
        i = 0
        for j in range(indexDifference, len(nums)):
            min_idx = min(i, min_idx, key=lambda x:nums[x]) # using nums[idx] as base to compare
            max_idx = max(i, max_idx, key=lambda x:nums[x])
            if nums[j] - nums[min_idx] >= valueDifference:
                return [min_idx, j]
            if nums[max_idx] - nums[j] >= valueDifference:
                return [max_idx, j]
            i += 1
        
        return no_answer
