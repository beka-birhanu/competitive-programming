# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        st = [(p,q)]

        while st:
            curr_p, curr_q = st.pop()
            if not curr_p and not curr_q:
                continue

            if not curr_p or not curr_q or curr_q.val != curr_p.val:
                return False

            st.append((curr_p.left, curr_q.left))
            st.append((curr_p.right, curr_q.right))
            
        return True