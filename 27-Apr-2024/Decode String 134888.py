# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        for S in s:
            if S != ']':
                stk.append(S)
            else:
                chrct = ''
                while stk[-1] != '[':
                    chrct = stk.pop() + chrct
                stk.pop()
                k = ''
                while stk and stk[-1].isdigit():
                    k = stk.pop() + k
                stk.append(chrct*int(k))
        return ''.join(stk)