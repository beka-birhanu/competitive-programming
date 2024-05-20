# Problem: Basic Calculator II - https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        rslt = crntNum = 0
        crntOpp = '+'
        nums = []
        opps = ['+', '-', '*', '/']
        for idx in range(len(s)):
            chrct = s[idx]
            if chrct.isdigit():
                crntNum = (crntNum * 10) + int(chrct)
            if  chrct in opps or idx == len(s)-1:
                if crntOpp == "+":
                    nums.append(crntNum)
                elif crntOpp == "-":
                    nums.append(-crntNum)
                elif crntOpp == "*":
                    nums[-1] *= crntNum
                elif crntOpp == '/':
                    nums[-1] = int(nums[-1] / crntNum)
                crntOpp = chrct
                crntNum = 0
        for ints in nums:
            rslt += ints
        return rslt