# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(node, ans):
            if not node:
                return ans
            
            inorder(node.left, ans)
            ans.append(node)
            inorder(node.right, ans)

            return ans
        

        def to_bst(l, r, nodes):
            if l > r:
                return None
            
            m = (l+r)//2
            root = nodes[m]

            root.left = to_bst(l, m-1, nodes)
            root.right = to_bst(m+1, r, nodes)

            return root

        sorted_node = inorder(root, [])
        
        return to_bst(0, len(sorted_node)-1, sorted_node)
