class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        mon_stack = []
        for Int in num:
            x = int(Int)
            while mon_stack and x < mon_stack[-1] and k:
                mon_stack.pop()
                k -= 1
            mon_stack.append(x)
        while mon_stack and k:
            mon_stack.pop()
            k -= 1
        return str(int(''.join(map(str,mon_stack)))) if mon_stack else '0'
