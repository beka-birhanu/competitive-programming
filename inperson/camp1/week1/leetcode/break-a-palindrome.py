class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""

        palindrome = list(palindrome)
        for i in range(len(palindrome)//2):
            if palindrome[i] != "a":
                palindrome[i] = "a"
                break
        
        else:
            for j in range(len(palindrome)-1,ceil(len(palindrome)/2)-1,-1):
                if palindrome[j] != "z":
                    palindrome[j] = chr(ord(palindrome[j])+1)
                    break
        return "".join(palindrome)
  