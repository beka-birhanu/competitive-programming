class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, curr_sum, ans, curr_comb, candidates, target):
            if curr_sum == target:
                ans.append(curr_comb.copy())
                return ans
            
            if start >= len(candidates) or curr_sum > target:
                return ans
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                curr_sum += candidates[i]
                curr_comb.append(candidates[i])
                backtrack(i+1, curr_sum, ans, curr_comb, candidates, target)

                curr_sum -= candidates[i]
                curr_comb.pop()

            return ans
        
        candidates.sort(reverse = True)
        return backtrack(0, 0, [], [], candidates, target)