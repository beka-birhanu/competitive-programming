class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(sub_sets, curr_sub_set, start_idx, num):
            sub_sets.append(curr_sub_set[:])

            if start_idx >= len(nums):
                return 
            
            for i in range(start_idx, len(nums)):
                curr_sub_set.append(nums[i])
                backtrack(sub_sets, curr_sub_set, i+1, num)
                curr_sub_set.pop()
            
        sub_sets = []

        backtrack(sub_sets, [], 0, nums)
        return sub_sets