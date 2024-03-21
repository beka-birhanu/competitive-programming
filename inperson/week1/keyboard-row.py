class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = "qwertyuiop"
        second = "asdfghjkl"
        third = "zxcvbnm"

        def possible(word:str)->bool:

            if word[0] in first:
                row = first
            elif word[0] in second:
                row = second
            else:
                row = third


            for letter in word:

                if letter not in row:
                    return False

            return True



        ans =[]
        for word in words:
            if possible(word.lower()):
                ans.append(word)

        return ans