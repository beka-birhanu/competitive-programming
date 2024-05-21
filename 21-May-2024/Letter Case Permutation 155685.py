# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        permutations = []
        char_indices = []
        
        for i, ch in enumerate(s):
            if ch not in '0123456789':
                char_indices.append(i)

        n = len(char_indices)
        for i in range(2**n):
            permutation = list(s.lower())
            j = 0
            
            while i > 0:
                is_on = i & 1
                if is_on:
                    idx = char_indices[j]
                    permutation[idx] = permutation[idx].upper()
                
                i >>= 1
                j +=1
            
            permutations.append("".join(permutation))
        
        return permutations