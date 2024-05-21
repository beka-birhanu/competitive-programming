# Problem: Minimum XOR Sum of Two Arrays - https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def dp(i, mask):
            if i >= len(nums1):
                return 0

            options = []
            for j, v in enumerate(nums2):
                if (1 << j) & mask == 0:
                    options.append((v ^ nums1[i]) + dp(i+1, mask | (1 << j)))

            return min(options)

        return dp(0, 0)


