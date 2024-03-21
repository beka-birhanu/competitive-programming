class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1

        pref_sum = 0
        ans = 0
        for num in nums:
            if num % 2:
                pref_sum += 1
            
            ans += dic[pref_sum-k]
            dic[pref_sum] += 1

        return ans