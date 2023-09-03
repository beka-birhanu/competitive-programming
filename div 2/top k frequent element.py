from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        for ke,va in Counter(nums).most_common():
            if k > 0:
                ans.append(ke)
                k -= 1
            else:
                return ans
        return ans
