class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        j = 0
        ans = []
        dic = {}
        dic1 = collections.Counter(p)

        for i in range(len(s)):
            if s[i] not in p:
                j = i + 1
                dic.clear()

            elif s[i] in p:

                if s[i] in dic:
                    dic[s[i]] += 1
                else:
                    dic[s[i]] = 1

                if i-j+1 > len(p):
                    dic[s[j]] -= 1
                    j += 1
                    
                if i-j+1 == len(p):
                    no = False
                    for chr,frq in dic.items():

                        if (chr in p and frq == dic1[chr]) or frq == 0:
                            continue
                        else:
                            no = True
                    if not no:
                        ans.append(j)
        return ans
