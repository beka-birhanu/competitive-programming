class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        DIGIT_MAP = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        ans = []
        curr = []

        def backtrack(start):
            if start >= len(digits):
                if curr:
                    ans.append("".join(curr))
                return 
                
            for letter in DIGIT_MAP[digits[start]]:
                curr.append(letter)
                backtrack(start+1)
                curr.pop()
        
        backtrack(0)
        return ans