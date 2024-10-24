# Problem: N-ary Tree Postorder Traversal - https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def helper(node, ans):
            if not node:
                return None
            
            for child in node.children:
                helper(child, ans)
            ans.append(node.val)

        ans = []
        helper(root, ans)
        return ans