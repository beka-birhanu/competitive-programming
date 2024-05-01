# Problem: Minimum Number of Operations to Make Array XOR Equal to K - https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = k
        for num in nums:
            xor ^= num
        
        return bin(xor)[2:].count("1")