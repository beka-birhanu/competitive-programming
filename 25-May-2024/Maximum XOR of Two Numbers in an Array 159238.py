# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        def insert(num, root):
            curr = root
            mask = 1 << 31
            max_int = (1<<32)-1
            
            for i in range(32):
                bit = 1 if num & mask > 0 else 0

                if bit not in curr:
                    curr[bit] = {}
                
                curr = curr[bit]
                num  = (num << 1) & max_int

        
        def get_max_xor(num, root):
            curr = root
            max_xor = 0
            idx = 31
            mask = 1 << 31
            max_int = (1<<32)-1

            while num > 0:
                bit = 1 if num & mask > 0 else 0

                if (1-bit) in curr:
                    max_xor += 1 << idx
                    curr = curr[1-bit]
                
                else:
                    curr = curr[bit]
                
                num  = (num << 1) & max_int
                idx -= 1
            
            return max_xor

        root = {}
        for num in nums:
            insert(num, root)

        return max(get_max_xor(num, root) for num in nums)