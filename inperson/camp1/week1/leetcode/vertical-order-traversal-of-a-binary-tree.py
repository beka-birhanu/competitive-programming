# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(root, position):
            nonlocal columns

            if not root:
                return 
            
            row, col = position
            columns[col].append((row, root.val))
            dfs(root.left, (row+1, col-1))
            dfs(root.right, (row+1, col+1))

        columns = defaultdict(list)

        dfs(root,(0,0))
        columns =[columns[key] for key in sorted(columns.keys())]

        for column in columns:
            column.sort()
            for i in range(len(column)):
                column[i] = column[i][1]
        return columns