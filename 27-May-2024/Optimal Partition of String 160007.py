# Problem: Optimal Partition of String - https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        N = len(s)
        char_freq = [0]*26
        substring_count = 0

        i = 0
        for j in range(N):
            idx = ord(s[j]) - ord('a')
            char_freq[idx] += 1

            if char_freq[idx] > 1:
                substring_count += 1

                while i < j:
                    left_idx = ord(s[i]) - ord('a')
                    char_freq[left_idx] -= 1
                    i += 1

        return substring_count + 1
