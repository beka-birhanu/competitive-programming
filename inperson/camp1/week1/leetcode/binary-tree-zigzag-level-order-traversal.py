# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        dq = deque([(root,0)])
        while dq:
            node, level = dq.popleft()
            if not node:
                continue

            if level % 2:
                if level+1 == len(ans):
                    ans[-1].appendleft(node.val)
                
                else:
                    ans.append(deque([node.val]))
            else:
                if level+1 == len(ans):
                    ans[-1].append(node.val)
                
                else:
                    ans.append(deque([node.val]))
            
            dq.append((node.left, level+1))
            dq.append((node.right, level+1))
        
        return ans