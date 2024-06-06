# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        total = curr = 0

        for c in s:
            if c == '1': 
                curr += 1
            else: 
                total += curr

        return total
