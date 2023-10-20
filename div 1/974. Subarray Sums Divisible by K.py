class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1

        pref_sum = 0
        ans = 0
        for num in nums:
            pref_sum += num
            
            ans += dic[pref_sum%k]
            dic[pref_sum%k] += 1

        return ans
