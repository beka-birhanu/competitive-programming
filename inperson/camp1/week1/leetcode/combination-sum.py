class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(start, curr_sum):
            if curr_sum == target:
                subsets.append(curr_subset[:])

            
            for i in range(start, len(candidates)):
                if curr_sum + candidates[i] > target:
                    continue

                curr_subset.append(candidates[i])
                backtrack(i, curr_sum + candidates[i])
                curr_subset.pop()

        candidates.sort()  
        subsets = []
        curr_subset = []

        backtrack(0, 0)

        return subsets