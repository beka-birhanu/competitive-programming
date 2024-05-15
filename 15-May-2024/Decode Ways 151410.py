# Problem: Decode Ways - https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        n = len(s)
        s_int = []

        for i in range(n):
            num = int(s[i])

            if num == 0:
                if s_int[-1] == 0 or s_int[-1] >= 3:
                    return 0
                else:
                    s_int[-1] *= 10
            
            else:
                s_int.append(num)
        
        n = len(s_int)
        curr = 1
        prev = 1

        for i in range(n-2, -1, -1):

            if (s_int[i] == 1 and s_int[i+1] < 10) or (s_int[i] == 2 and s_int[i+1] < 7):
                curr, prev = curr + prev, curr
            
            else:
                prev = curr
                
        return curr
            