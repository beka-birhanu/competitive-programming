class Solution:
    def longestPalindrome(self, s: str) -> int:
        freqs = Counter(s)
        length = 0
        seen_odd = False #to determine if odd freq is present n freqs
        for key,val in freqs.items():
            if not val % 2:
                length += val
            else:
                length += val -1
                seen_odd = True
        
        return length + (1 if seen_odd else 0)