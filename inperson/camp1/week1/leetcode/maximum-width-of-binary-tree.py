# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dq = deque([(root, 0, 1)])
        level = 1
        max_width = 0
        curr_far_left = 1
        curr_far_right = 1

        while dq:
            curr_node, curr_level, curr_node_num = dq.popleft()
            if not curr_node:
                continue
            
            if curr_level == level:
                curr_far_left = min(curr_far_left, curr_node_num)
                curr_far_right = max(curr_far_right, curr_node_num)


            else:
                curr_far_left = curr_node_num
                curr_far_right = curr_node_num
                level = curr_level
            
            max_width = max(max_width, (curr_far_right - curr_far_left + 1))

            dq.append((curr_node.left, level + 1, curr_node_num * 2))
            dq.append((curr_node.right, level + 1, curr_node_num * 2 +1))
        
        return max_width

