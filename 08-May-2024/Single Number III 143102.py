# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def checkBit(self, n, i):
        return (n & (1<<i))!=0
    
    def getSetBitPos(self, n):
        for i in range(32):
            if self.checkBit(n, i):
                return i
    
    def singleNumber(self, nums: List[int]) -> List[int]:
        x,n = 0,len(nums)
        if n==2:
            return nums
        
        for i in range(n):
            x^=nums[i]
        
        pos = self.getSetBitPos(x)
        x1,x2 = 0,0
        for i in range(n):
            if self.checkBit(nums[i],pos):
                x1^=nums[i]
            else:
                x2^=nums[i]
        
        return [x1, x2]