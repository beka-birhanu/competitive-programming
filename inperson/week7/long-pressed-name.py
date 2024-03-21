class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # letters that can be typed
        letter_domain = set(name)

        # points to the last correctly typed letter
        p1 = 0 

        for c in typed:
            if c not in letter_domain:
                return False
            
            if p1 < len(name) and name[p1] == c:
                p1 += 1

            elif p1 == 0 and name[p1] != c:
                return False

            elif 0 < p1 <= len(name) and name[p1-1] != c:
                return False

        return p1 == len(name)