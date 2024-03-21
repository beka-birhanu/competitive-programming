# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        res = [0]
        def check(node):
            if not node: return 0, True, -inf, inf
            
            sl, bstl, maxl, minl = check(node.left)
            sr, bstr, maxr, minr = check(node.right)
            
            if bstl and bstr and maxl < node.val < minr:
                v = node.val + sl + sr
                res[0] = max(res[0], v)
                return v, True, max(maxr, node.val), min(node.val, minl)
            
            return 0, False, -inf, inf
        
        check(root)
        return res[0]