class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opens = 0
        ops = 0 #the min oprations to be preformed
        for par in s:
            if par == "(":
                opens += 1
            else:
                if not opens:
                    ops += 1
                else:
                    opens -= 1
        return ops + opens