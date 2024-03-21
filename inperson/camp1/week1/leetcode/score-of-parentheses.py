class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        OPEN = "("
        st = [0]
        for parenthesis in s:
            if parenthesis == OPEN:
                st.append(parenthesis)
            else:
                curr_score = 1

                if st[-1] != OPEN:
                    curr_score = st.pop() * 2

                st.pop() #remove the inclosing open bracket
                if st[-1] != OPEN:
                    curr_score += st.pop()

                st.append(curr_score)
        return st[0]