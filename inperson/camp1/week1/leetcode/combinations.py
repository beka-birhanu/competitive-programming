class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combination = []
        combinations = []
        def backtracking(n, k, startIndex):
            if len(combination) == k:
                combinations.append(combination[:])
                return
            
            for i in range(startIndex, n - (k-len(combination)) + 2):
                combination.append(i)
                backtracking(n, k, i+1)
                combination.pop()
        

        backtracking(n, k, 1)

        return combinations
                