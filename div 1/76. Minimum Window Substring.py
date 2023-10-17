# Runtime 375 ms and Memory 17.4 MB

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        dict_s = collections.Counter(s)
        dict_t = collections.Counter(t)
        seen = {}

        for key,val in dict_t.items():
            if key not in dict_s:
                return ""
            elif val > dict_s[key]:
                return ""

            seen[key] = 0

        dic = {}

        ans = [0,len(s)+1]
        i = 0
        for j,cr in enumerate(s):
            if cr in dict_t:
                seen[cr] += 1
                if cr not in dic:
                    dic[cr] = collections.deque([j])
                else:
                    dic[cr].append(j)
                    while seen[cr] > dict_t[cr]:
                        dic[cr].popleft()
                        seen[cr] -= 1
                    
            
            if seen == dict_t:
                i = min(x[0] for x in dic.values())
                if ans[1] - ans[0]  > j-i:
                    ans = [i,j]
        return "" if ans[1] > len(s) else s[ans[0]:ans[1]+1]
