# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        N = len(nums)
        total_sum = sum(nums)
        
        i = 0
        window_sum = 0
        min_op = N+1

        for j in range(N):
            window_sum += nums[j]

            while total_sum - window_sum < x and i <= j:
                window_sum -= nums[i]
                i += 1
            
            if total_sum - window_sum == x:
                min_op = min(min_op, N - (j-i+1))
        
        return min_op if min_op < N + 1 else -1