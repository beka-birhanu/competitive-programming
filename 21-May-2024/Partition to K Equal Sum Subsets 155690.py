# Problem: Partition to K Equal Sum Subsets - https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        target = sum(nums) / k

        if N < k or target % 1: 
            return False
        
        nums.sort(reverse = True)
        if nums[0] > target:
            return False

        @cache 
        def dp(mask, cur):
            if mask == 0: 
                return cur == 0
            elif cur == 0: 
                return dp(mask, target)

            for bit in range(len(nums)):
                if mask & (1 << bit):
                    if nums[bit] <= cur and dp(mask ^ (1 << bit), cur-nums[bit]):
                        return True

            return False
    
        return dp(2**N-1, target)