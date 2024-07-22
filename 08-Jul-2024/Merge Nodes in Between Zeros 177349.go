# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode MergeNodes(ListNode head) {
        void merge(ListNode startNode) {
            if(startNode == null){
                return;
            }
            ListNode next = startNode.next;

            while(next.val != 0) {
                startNode.val += next.val;
                next = next.next;
            }

            startNode.next = next;
            return;
        }

        var dummy = new ListNode(0, head);
        var curr = dummy;

        while (curr != null) {
            curr.next = curr.next.next;
            merge(curr.next);
            curr = curr.next;
        }
        return dummy.next;
    }
}