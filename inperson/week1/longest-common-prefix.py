class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        max_len = len(ans)
        for i in range(1,len(strs)):
            this_len = 0
            for j in range(len(strs[i])):
                if j >= len(ans):
                    break
                elif ans[j] != strs[i][j]:
                    break
                elif  ans[j] == strs[i][j]:
                    this_len += 1

            max_len = min(max_len,this_len)
        
        return ans[:max_len]