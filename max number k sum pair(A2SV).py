from collections import Counter
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        counter = Counter(nums)
        ans = 0
        for _ in range(len(nums)):
            sub = nums[_]
            if sub <= (k // 2 + 1):
                if k-sub == sub:
                    if counter[sub] >= 2:
                        counter[sub] -= 2
                        ans += 1
                elif counter[k-sub] > 0 and counter[sub] > 0:
                    counter[sub] -= 1
                    counter[k-sub] -= 1
                    ans += 1
            else:
                return ans
        return ans

    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        i, j = 0, len(nums)-1
        while i < j:
            if nums[i] + nums[j] ==  k:
                ans += 1
                i += 1
                j -= 1
            elif nums[i] + nums[j] > k:
                j -= 1
            else:
                i += 1
        return ans
