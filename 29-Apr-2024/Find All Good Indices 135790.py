# Problem: Find All Good Indices - https://leetcode.com/problems/find-all-good-indices/

class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        non_decreasing_count = [1] * n
        non_increasing_count = [1] * n

        # build non increasing count using prefix concept 
        for i in range(1, n):
            if nums[i] <= nums[i-1]:
                non_increasing_count[i] += non_increasing_count[i-1]
        
        # build non decreasing count using postfix concept
        for i in range(n-2, -1, -1):
            if nums[i] <= nums[i+1]:
                non_decreasing_count[i] += non_decreasing_count[i+1]
        

        good_idx = []

        for i in range(k, n-k):
            # if there is k non increasing order just before it
            # and if there is k non decreasing order just after it
            if non_increasing_count[i-1] >= k and non_decreasing_count[i+1] >= k:
                good_idx.append(i)
        
        return good_idx
        