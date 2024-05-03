# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        _max = 2**maximumBit
        xor = 0
        for num in nums:
            xor ^= num
        
        query_result = []
        for num in reversed(nums):
            inverse = ~xor
            k = inverse % _max
            
            query_result.append(k)
            xor ^= num
        
        return query_result
            

