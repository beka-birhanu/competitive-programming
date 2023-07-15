class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        ans = 0
        i = 0
        for j in range(len(s)):
            if s[j] in dic and i <= dic.get(s[j]):
                i = dic.get(s[j]) + 1
            dic[s[j]] = j
            ans = max(ans,j-i+1)
        
        return ans

    #using set as it has faster hashing opration than dictionary
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = set()
        ans = 0
        i = 0
        
        for j in range(len(s)):
            if s[j] not in dic:
                dic.add(s[j])
                ans = max(ans,len(dic))
            else:
                while s[j] in dic:
                    dic.remove(s[i])
                    i += 1

                dic.add(s[j])
        
        return ans
