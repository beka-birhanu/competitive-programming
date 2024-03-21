class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sub_count = 0
        prefs= defaultdict(int)
        prefs[0] = 1

        pref = 0
        for num in nums:
            pref += num
            sub_count += prefs[pref - goal]
            prefs[pref] += 1

        return sub_count