# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def check(str1, str2):
            diff_count = 0
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    diff_count += 1

                    if diff_count > 2:
                        return False
            
            return True
        
        def find(groups, i):
            while groups[i] != i:
                groups[i] = groups[groups[i]]
                i = groups[i]
            
            return i
        
        n = len(strs)
        groups = [i for i in range(n)]

        for i, str1 in enumerate(strs):
            group1 = find(groups, i)
            for j, str2 in enumerate(strs):
                group2 = find(groups, j)
                if check(str1, str2):
                    groups[group2] = group1
        
        return len(set(groups))

