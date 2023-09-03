class Solution:
    def reverseString(self, s: list[str],i:int = 0,j:int = -1) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if j < 0:
            j = len(s)
        if j >=2 and i < j:
            s[i],s[j-1] = s[j-1],s[i]
            self.reverseString(s,i+1,j-1)
    def reverseString_iterative(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1
        while i < j:
            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1
