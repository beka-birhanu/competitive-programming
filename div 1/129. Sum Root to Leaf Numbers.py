
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Runtime 43ms , Memory 16.2mb
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sum = 0
        stack = [(root,root.val)]
        while stack:
            r,val = stack.pop()
            right = r.right
            left = r.left
            if not (right or left):
                sum += val
            if right:
                stack.append((right,right.val+(val*10)))
            if left:
                 stack.append((left,left.val+(val*10)))
        return sum
