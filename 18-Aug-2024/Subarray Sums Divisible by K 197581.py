# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prev_remainders_count = defaultdict(int)

        prev_remainders_count[0] = 1
        subarray_count = 0
        running_sum = 0

        for num in nums:
            running_sum += num
            remainder = running_sum % k

            subarray_count += prev_remainders_count[remainder]
            prev_remainders_count[remainder] += 1
        
        return subarray_count
