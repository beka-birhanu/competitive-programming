class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1

        pref = 0
        ans = 0
        for num in nums:
            pref += num

            ans += dic[pref%k]
            dic[pref%k] += 1

        return ans 

