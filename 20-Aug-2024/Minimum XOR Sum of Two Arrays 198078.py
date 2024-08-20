# Problem: Minimum XOR Sum of Two Arrays - https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def dp(i, mask):
            if i >= len(nums1):
                return 0
            
            _min = inf
            for j in range(len(nums2)):
                if not mask & 1 << j:
                    _min = min(_min, (nums1[i]^nums2[j])+dp(i+1, mask|1<<j))
            
            return _min
        
        return dp(0, 0)