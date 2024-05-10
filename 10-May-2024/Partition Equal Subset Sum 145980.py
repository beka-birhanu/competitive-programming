# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total&1:
            return False # its odd 

        subSetsum = total >> 1 
        bitMask = 1
        for n in nums:
            bitMask = bitMask | bitMask << n 
            
        return bitMask & 1 << subSetsum