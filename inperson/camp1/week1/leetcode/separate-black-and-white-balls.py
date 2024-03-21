class Solution:
    def minimumSteps(self, s: str) -> int:
        swaps = 0
        ones = 0
        for i in s:
            if i == "1":
                ones += 1
                continue
            swaps += ones
        return swaps
