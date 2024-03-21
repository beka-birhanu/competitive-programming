class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        right_most = {}
        for i, c in enumerate(s):
            right_most[c] = i
        
        ans = []
        l = r = 0
        for i, c in enumerate(s):
            r = max(r, right_most[c])

            if i == r:
                ans.append(r - l + 1)
                l = r + 1
        
        return ans
            