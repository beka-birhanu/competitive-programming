# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def find_leaf(root, is_right):
            if not is_right:
                if not root.left:
                    return root.val
                return find_leaf(root.left, is_right)
            else:
                if not root.right:
                    return root.val
                return find_leaf(root.right, is_right)
        
        if not root:
            return True

        left = -inf if not root.left else find_leaf(root.left, True)
        right = inf if not root.right else find_leaf(root.right, False)

        if not(left < root.val < right):
            return False
        
        return self.isValidBST(root.left) and self.isValidBST(root.right)