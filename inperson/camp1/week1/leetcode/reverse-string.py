class Solution:
    def reverseString(self, s: List[str]) -> None:
        def reverse_margines(s,i,j):
            if i >= j:
                return
            s[i], s[j] = s[j], s[i]
            reverse_margines(s,i+1,j-1)

        reverse_margines(s,0,len(s)-1)
        """
        Do not return anything, modify s in-place instead.
        """
        