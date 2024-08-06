# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# NamedTuple to store the found node type and the path
class FoundNodeTypeWithPath(NamedTuple):
    node_found: int
    path: str

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        DIRECTIONS = {"left": "L", "right": "R", "up": "U"}
        NEITHER = -1
        START = 0
        DEST = 1
        BOTH = 2

        def helper(node, start_value, dest_value):
            if not node:
                return FoundNodeTypeWithPath(NEITHER, "")
            
            left = helper(node.left, start_value, dest_value)
            if left.node_found == BOTH:
                return left

            right = helper(node.right, start_value, dest_value)
            if right.node_found == BOTH:
                return right

            start = FoundNodeTypeWithPath(NEITHER, "")
            dest = FoundNodeTypeWithPath(NEITHER, "")

            if left.node_found == START:
                start = FoundNodeTypeWithPath(START, DIRECTIONS['up'] + left.path)
            elif right.node_found == START:
                start = FoundNodeTypeWithPath(START, DIRECTIONS['up'] + right.path)
            elif node.val == start_value:
                start = FoundNodeTypeWithPath(START, "")

            if left.node_found == DEST:
                dest = FoundNodeTypeWithPath(DEST, DIRECTIONS['left'] + left.path)
            elif right.node_found == DEST:
                dest = FoundNodeTypeWithPath(DEST, DIRECTIONS['right'] + right.path)
            elif node.val == dest_value:
                dest = FoundNodeTypeWithPath(DEST, "")

            if start.node_found == START and dest.node_found == DEST:
                return FoundNodeTypeWithPath(BOTH, start.path + dest.path)

            return start if start.node_found == START else dest

        return helper(root, startValue, destValue).path