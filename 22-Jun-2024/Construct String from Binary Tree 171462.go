# Problem: Construct String from Binary Tree - https://leetcode.com/problems/construct-string-from-binary-tree/description/

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
    public string Tree2str(TreeNode root) {
        if (root != null) {
            if (root.right != null)
                return $"{root.val}({Tree2str(root.left)})({Tree2str(root.right)})";

            else if (root.left != null)
                return $"{root.val}({Tree2str(root.left)})";

            else
                return $"{root.val}";
        }
        return null;
    }
}