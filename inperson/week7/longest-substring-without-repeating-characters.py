class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        
        seen_at = defaultdict(list)
        longest_uniqe = 0

        for end in range(len(s)):

            if seen_at[s[end]] and seen_at[s[end]][-1] >= start:
                start = seen_at[s[end]][-1]+1
            seen_at[s[end]].append(end)
            
            longest_uniqe = max(longest_uniqe,end-start+1)
        return longest_uniqe