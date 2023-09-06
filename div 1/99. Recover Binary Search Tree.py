# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Runtime 61 ms and Memory 16.5mb
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
      """
      Do not return anything, modify root in-place instead.
      """
      first = None
      second = None 
      prev = None
      pred = None 
      
      curr = root 
      while curr:
        if not curr.left:

          if prev and curr.val < prev.val:
            if not first: first = prev
            second = curr
          prev = curr
          curr = curr.right
        else:

          pred = curr.left
          while pred.right and pred.right != curr:
            pred = pred.right
          
          if not pred.right:

            pred.right = curr
            curr = curr.left
          else:

            pred.right = None
            if prev and curr.val < prev.val:
              if not first: first = prev
              second = curr
            prev = curr
            curr = curr.right
      

      first.val, second.val = second.val, first.val
