class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(permutations, curr_permutaion: list, used: set, nums:list):
            if len(curr_permutaion) == len(nums):
                permutations.append(curr_permutation[:])
                return 
            
            for num in nums:
                if num not in used:
                    curr_permutation.append(num)
                    used.add(num)

                    backtrack(permutations, curr_permutaion, used, nums)
                    
                    curr_permutaion.pop()
                    used.remove(num)

        permutations = []
        curr_permutation = []

        backtrack(permutations, curr_permutation, set(), nums)

        return permutations