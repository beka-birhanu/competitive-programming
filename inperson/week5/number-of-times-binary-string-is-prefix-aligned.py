class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        max_idx = 0
        count = 0
        for i in range(len(flips)):
            max_idx = max(flips[i],max_idx)
            if max_idx-1 == i:
                count += 1
        return count