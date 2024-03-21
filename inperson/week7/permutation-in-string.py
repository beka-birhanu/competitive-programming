class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict1 = collections.Counter(s1)

        left = len(s1)
        window_size = len(s1)

        for j,chr in enumerate(s2):
            if chr in dict1:
                if dict1[chr] > 0:
                    left -= 1
                dict1[chr] -= 1

            if j >= window_size:
                if s2[j-window_size] in dict1:
                    dict1[s2[j-window_size]] += 1
                    if dict1[s2[j-window_size]] > 0:
                        left += 1

            if not left:
                return True
                
        return False