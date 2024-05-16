# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        ops = 0
        i, j = 0, len(nums)-1

        while i < j:
            _sum = nums[i] + nums[j] 

            if _sum == k:
                ops += 1
                i += 1
                j -= 1
            
            elif _sum < k:
                i += 1
            
            else: 
                j -= 1
        
        return ops