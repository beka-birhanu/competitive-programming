class Solution:
    def numberOfWays(self, s: str) -> int:
        total = Counter(s)
        valid_ways = 0
        pre_zeros = 0
        pre_ones = 0

        for c in s:
            if c == "0":
                valid_ways += (total["1"] - pre_ones) * pre_ones
                pre_zeros += 1
            else:
                valid_ways += (total["0"] - pre_zeros) * pre_zeros
                pre_ones += 1

        return valid_ways