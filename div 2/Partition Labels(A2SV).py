class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ref = collections.Counter(s)
        check = []
        ans = []
        i = 0
        for j in range(len(s)):
            
            if ref[s[j]] < 0:
                ref[s[j]] += 1
            elif ref[s[j]] > 0:
                ref[s[j]] = -( ref[s[j]]-1)
                check.append(1)
            if ref[s[j]] == 0:
                check.pop()

            if len(check) == 0:
                ans.append(j-i+1)
                i = j + 1

        return ans
