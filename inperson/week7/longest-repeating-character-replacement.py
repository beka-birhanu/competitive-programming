class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_dict = {letter: 0 for letter in 'QWERTYUIOPASDFGHJKLZXCVBNM'}
        
        j = 0
        max_len = 0
        max_rep = 0

        for i,chr in enumerate(s):
            freq_dict[chr] += 1
            max_rep = max(max_rep,freq_dict[chr])

            if i-j+1 - max_rep <= k:
                max_len = max(max_len,i-j + 1)

            else:
                freq_dict[s[j]] -= 1
                j += 1

        return max_len