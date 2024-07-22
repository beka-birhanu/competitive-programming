# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public bool IsSymmetric(TreeNode root) {
        bool isSame(TreeNode subTree1, TreeNode subTree2) {
            if (subTree1 == null && subTree2 == null) {
                return true;
            }
            if (subTree1 == null || subTree2 == null) {
                return false;
            }

            return subTree1.val == subTree2.val && isSame(subTree1.right, subTree2.left) && isSame(subTree1.left, subTree2.right);
        }

        return isSame(root.left, root.right);
    }
}