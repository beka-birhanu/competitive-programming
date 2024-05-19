# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map = defaultdict(lambda : 'A')
        seen = set()

        for i in range(len(s)):
            char_1 = s[i]
            char_2 = t[i]
            if (char_map[char_1] != "A" or char_2 in seen) and char_map[char_1] != char_2:
                return False
            
            char_map[char_1] = char_2
            seen.add(char_2)
        
        return True

