# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        st = [root]
        while st:
            curr = st.pop()
            if not curr or curr.val == val:
                return curr

            st.append(curr.left if curr.val > val else curr.right)