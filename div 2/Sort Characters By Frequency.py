from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        dict_of_s = Counter(s)
        ans = ""
        for key,val in sorted(dict_of_s.items(),key= lambda x: x[1],reverse=True):
            ans += key * val
        return ans
