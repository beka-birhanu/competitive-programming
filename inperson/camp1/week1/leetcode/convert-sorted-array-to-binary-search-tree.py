# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def toSubTree(l, r, nums) ->  Optional[TreeNode]:
            if l > r:
                return None

            m = (r+l)//2
            sub_root = TreeNode(nums[m])

            sub_root.left = toSubTree(l, m-1, nums)
            sub_root.right = toSubTree(m+1, r, nums)

            return sub_root

        m = (len(nums)-1)//2

        root = TreeNode(nums[m])
        root.left = toSubTree(0, m-1, nums)
        root.right = toSubTree(m+1, len(nums)-1, nums)

        return root
