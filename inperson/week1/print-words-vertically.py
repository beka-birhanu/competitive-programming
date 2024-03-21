class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = list(s.split())
        ans = [""]*len(max(s,key = lambda x: len(x)))
        for i in range(len(ans)):
            temp = ''
            for j in range(len(s)):

                if len(s[j]) > i:
                    temp += " "*(j-len(temp)) + s[j][i]
            ans [i] = temp
        return ans
                