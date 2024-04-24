# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:

    l1 = [0,1,1]

    def tribonacci(self, n: int) -> int:
        if len(self.l1)<=n:
            while len(self.l1)<=n:
                self.l1.append(self.l1[-1]+self.l1[-2]+self.l1[-3])
        
        return self.l1[n]
            