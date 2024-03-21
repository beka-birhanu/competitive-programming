# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root) -> list[int]:
            nonlocal max_freq, modes, prev_node, cur_freq
            if not root:
                return 
            dfs(root.left)
            if root.val == prev_node:
                cur_freq += 1
            else:
                cur_freq = 1
                prev_node = root.val
            
            if cur_freq == max_freq:
                modes.append(root.val)
            
            elif cur_freq > max_freq:
                modes = [root.val]
                max_freq = cur_freq
            dfs(root.right)

        modes = []
        cur_freq = 0
        max_freq = 0
        prev_node = inf

        dfs(root)
        return modes