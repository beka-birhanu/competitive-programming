# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find(parents, idx):
            while parents[idx] != idx:
                parents[idx] = parents[parents[idx]]
                idx = parents[idx]
            
            return idx
        
        def union(parents, idx1, idx2):
            idx1_parent = find(parents, idx1)
            idx2_parent = find(parents, idx2)

            if idx1_parent <= idx2_parent:
                parents[idx2_parent] = idx1_parent
            
            else:
                parents[idx1_parent] = idx2_parent

        n = len(s1)
        parents = [i for i in range(26)]
        
        for i in range(n):
            idx1 = ord(s1[i]) - ord('a')
            idx2 = ord(s2[i]) - ord('a')

            union(parents, idx1, idx2)
    
        equivalent_string = []
        
        for letter in baseStr:
            idx = ord(letter) - ord('a')
            parent = find(parents, idx)

            min_equivalent_letter = chr(parent + ord('a'))
            equivalent_string.append(min_equivalent_letter)
        
        return "".join(equivalent_string)
