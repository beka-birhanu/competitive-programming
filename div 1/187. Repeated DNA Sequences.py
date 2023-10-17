# Runtime 64ms and Memory 28.56MB
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = set()
        seen = set()
        sub = ""
        for nuc in s:
            if len(sub) < 10:
                sub += nuc
            else:
                sub = sub[1:] + nuc
            if sub in seen:
                ans.add(sub)
            elif len(sub) == 10:
                seen.add(sub)
            
        return list(ans)
