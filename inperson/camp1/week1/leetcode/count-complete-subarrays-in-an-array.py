class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        window = Counter()
        unique_count = len(set(nums))
        complete = 0
        i = 0
        for j in range(len(nums)):
            window[nums[j]] += 1

            while window[nums[i]] > 1:
                window[nums[i]] -= 1
                i += 1

            if len(window) == unique_count:
                complete += i+1

        return complete
