# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def traverse(node, max_val, min_val):
            if not node:
                return max_val - min_val

            max_val = max(node.val, max_val)
            min_val = min(node.val, min_val)                

            left = traverse(node.left, max_val, min_val)
            right = traverse(node.right, max_val, min_val)

            return max(left, right)
            

        return traverse(root, root.val, root.val)