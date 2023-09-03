from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        ans = 0
        sum = 0
        for k,v in Counter(arr).most_common():
            sum += v
            ans += 1
            if len(arr)  <= 2 * sum:
                return ans
