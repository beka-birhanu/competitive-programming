# Problem: Compare Version Numbers - https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_revisions = list(map(int, version1.split(".")))
        version2_revisions = list(map(int, version2.split(".")))

        while version1_revisions and version1_revisions[-1] == 0:
            version1_revisions.pop()
        
        while version2_revisions and version2_revisions[-1] == 0:
            version2_revisions.pop()
        
        
        min_n = min(len(version1_revisions), len(version2_revisions))

        for i in range(min_n):
            version1_revision = version1_revisions[i]
            version2_revision = version2_revisions[i]

            if version1_revision < version2_revision:
                return -1
            
            elif version1_revision > version2_revision:
                return 1
        
        # if there is not trailing zeros and they are the same up to the length of the shortes one
        # then the comparison is all about the length
        if len(version1_revisions) < len(version2_revisions):
            return -1
        
        elif len(version1_revisions) > len(version2_revisions):
            return 1
        
        else:
            return 0
