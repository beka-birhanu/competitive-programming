# Problem: Number of Good Leaf Nodes Pairs - https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:

        def helper(node, depth, distance):
            nonlocal good_pair

            if not node:
                return []
            
            if not(node.right or node.left):
                return [(depth, 1)]
            
            left_depth_count = helper(node.left, depth+1, distance)
            right_depth_count = helper(node.right, depth+1, distance)
            
            for left_depth, left_count in left_depth_count:
                for right_depth, right_count in right_depth_count:
                    path_length = left_depth + right_depth -2*depth

                    if path_length <= distance:
                        good_pair += left_count * right_count
            
            return combine(left_depth_count, right_depth_count)


        def combine(pair1, pair2):
            combined_leaves = {}
            for depth, count in pair1:
                combined_leaves[depth] = combined_leaves.get(depth, 0) + count

            for depth, count in pair2:
                combined_leaves[depth] = combined_leaves.get(depth, 0) + count
            
            return [(depth, count) for depth, count in combined_leaves.items()]


        good_pair = 0
        helper(root, 0, distance)

        return good_pair

