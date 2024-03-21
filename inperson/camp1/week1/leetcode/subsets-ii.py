class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(subsets, curr_subset, start_idx, num):
            subsets.append(curr_subset[:])

            if start_idx >= len(nums):
                return 
            
            for i in range(start_idx, len(nums)):
                if i > start_idx and nums[i] == nums[i-1]:
                    continue
                
                curr_subset.append(nums[i])
                backtrack(subsets, curr_subset, i+1, num)
                curr_subset.pop()

        nums.sort() 
        subsets = []

        backtrack(subsets, [], 0, nums)
        return subsets