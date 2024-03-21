class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cols = [0]*len(strs[0])
        for i in range(1,len(strs)):
            for j in range(len(strs[0])):
                if strs[i][j] < strs[i-1][j]:
                    cols[j] = 1
        return cols.count(1)