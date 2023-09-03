class Solution:
    def reverseParentheses(self, s: str) -> str:
        before_sub = []
        for c in s:
            if c != ')':
                before_sub.append(c)
            else:
                temp_sub = []
                while before_sub[-1]!='(' and before_sub:
                    temp_sub.append(before_sub.pop())
                before_sub.pop()
                before_sub += temp_sub
        return ''.join(before_sub)
