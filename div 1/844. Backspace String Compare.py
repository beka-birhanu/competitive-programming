class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        s2 = []
        for c in s:
            if c =="#":
                if s1:
                    s1.pop()
            else:
                s1.append(c)
        for x in t:
            if x =="#":
                if s2:
                    s2.pop()
            else:
                s2.append(x)

        return s1 == s2
