# Problem: Maximum Depth of N-ary Tree - https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

/*
// Definition for a Node.
public class Node {
    public int val;
    public IList<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, IList<Node> _children) {
        val = _val;
        children = _children;
    }
}
*/

public class Solution {
    public int MaxDepth(Node root) {
        if (root == null){
            return 0;
        }
        Stack<Tuple<Node, int>> stack = new Stack<Tuple<Node, int>>();
        int maxDepth = 0;

        stack.Push(new Tuple<Node, int>(root, 1));
        while (stack.Count > 0){
            var (currNode, currDepth) = stack.Pop();
            maxDepth = Math.Max(maxDepth, currDepth);

            foreach(Node child in currNode.children){
                stack.Push(new Tuple<Node, int>(child, currDepth+1));
            }
        }
        return maxDepth;
}}