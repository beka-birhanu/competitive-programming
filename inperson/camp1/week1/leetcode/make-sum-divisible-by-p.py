class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        unwanted_sum = total % p
        if not unwanted_sum:
            return 0
        
        min_len = len(nums)
        pref_sums = {0:-1} # for cases when the sub array should start from the beging
        print(total, unwanted_sum)
        pref_sum = 0
        for i, num in enumerate(nums):
            pref_sum += num

            if (pref_sum - unwanted_sum) % p in pref_sums:
                min_len = min(min_len, i - pref_sums[(pref_sum - unwanted_sum) % p])

            pref_sums[pref_sum % p] = i
        
        return min_len if min_len < len(nums) else -1

