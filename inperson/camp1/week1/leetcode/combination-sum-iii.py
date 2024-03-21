class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, curr_sum, ans, curr_comb, k, n):
            if curr_sum == n and len(curr_comb) == k:
                ans.append(curr_comb.copy())
                return ans
            
            if curr_sum > n or len(curr_comb) >= k:
                return ans
            
            for i in range(start, 10):

                curr_sum += i
                curr_comb.append(i)
                backtrack(i+1, curr_sum, ans, curr_comb, k, n)

                curr_sum -= i
                curr_comb.pop()

            return ans
        

        return backtrack(1, 0, [], [], k, n)