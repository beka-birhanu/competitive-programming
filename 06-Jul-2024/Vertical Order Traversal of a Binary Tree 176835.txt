# Problem: Vertical Order Traversal of a Binary Tree - https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

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
    
    public IList<IList<int>> VerticalTraversal(TreeNode root) {
        SortedDictionary<int, SortedDictionary<int, IList<int>>> map = new();
        List<IList<int>> result = new();

        DFS(root, 0, 0, map);

        foreach(var item in map)
        {
            result.Add(item.Value.Values.SelectMany(x=>x.OrderBy(v=>v)).ToList());
        }
        return result;
    }

    private void DFS(TreeNode node, int row, int col, SortedDictionary<int, SortedDictionary<int, IList<int>>> map)
    {
        if(node == null)
        {
            return;
        }
        map.TryAdd(col, new SortedDictionary<int, IList<int>>());
        map[col].TryAdd(row, new List<int>());
        map[col][row].Add(node.val);

        DFS(node.left, row + 1, col - 1, map);
        DFS(node.right, row + 1, col + 1, map);
    }
}