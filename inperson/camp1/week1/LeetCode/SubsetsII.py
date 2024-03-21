class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(subsets, curr_subset, start_idx, num, seen):
            subsets.add(tuple(curr_subset))

            if start_idx >= len(nums):
                return 
            
            for i in range(start_idx, len(nums)):
                if tuple(curr_subset + [nums[i]]) not in seen:
                    curr_subset.append(nums[i])
                    seen.add(tuple(curr_subset))
                    backtrack(subsets, curr_subset, i+1, num, seen)
                    curr_subset.pop()

        nums.sort() 
        subsets = set()
        seen = set()

        backtrack(subsets, [], 0, nums, seen)
        return subsets