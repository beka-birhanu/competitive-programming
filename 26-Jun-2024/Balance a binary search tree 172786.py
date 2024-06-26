# Problem: Balance a binary search tree - https://leetcode.com/problems/balance-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        nodes = []

        def traversal(node):
            if node:
                traversal(node.left)
                nodes.append(node)
                traversal(node.right)
        traversal(root)

        def balance(nodes, start, end):
            if start > end:
                return None

            mid = (start+end) // 2
            node = nodes[mid]

            node.left = balance(nodes, start, mid - 1)
            node.right = balance(nodes, mid + 1, end)

            return node
            
        return balance(nodes, 0, len(nodes)-1)