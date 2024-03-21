# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        st = [(root,p,q)]
        while st:
            root, p, q = st.pop()
            if root.val == p.val or root.val == q.val:
                return root
                
            if root.val > p.val and root.val < q.val:
                return root

            if root.val > q.val and root.val < p.val:
                return root
            
            st.append((root.left, p, q) if root.val > q.val else (root.right, p, q))
            