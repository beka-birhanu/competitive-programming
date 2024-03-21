class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        q = deque([(0,0,"")])
        while q:
            o, c, parantheses = q.popleft()
            if o < n:
                q.append([o+1, c, parantheses+"("])
            if c < o:
                q.append([o, c+1, parantheses+")"])
            if o == c == n:
                ans.append(parantheses)

        return ans