class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict1 = collections.Counter(s1)
        i = 0
        left = (len(s1))
        for j,chr in enumerate(s2):
            if chr in dict1:
                if dict1[chr] > 0:
                    left -= 1
                dict1[chr] -= 1

            if j - i + 1 > len(s1):
                if s2[i] in dict1:
                    dict1[s2[i]] += 1
                    if dict1[s2[i]] > 0:
                        left += 1
                i += 1
            if not left:
                return True
        return False
