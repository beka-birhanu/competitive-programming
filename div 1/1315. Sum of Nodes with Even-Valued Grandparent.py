class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        s = [(root,1)]
        sum = 0
        while s:
            r , p = s.pop()
            left = r.left
            right = r.right
            if left:
                s.append((left,r.val))
                if p % 2 == 0:
                    sum += left.val
            if right:
                s.append((right,r.val))
                if p % 2 == 0:
                    sum += right.val
        return sum
