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
        if(root == null) {
            return "";
        }

        string left = this.Tree2str(root.left);
        string right = this.Tree2str(root.right);

        string ans = root.val.ToString();
        if(left != "") {
            ans += "(" + left + ")";
        }
        if (right != "") {
            if(left == "") {
                ans += "()";
            }
            ans += "(" + right + ")";
        }

        return ans;
    }
} 