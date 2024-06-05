# Problem: Maximum Twin Sum of Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast, slow = head, head
        prev = None

        while fast and fast.next :
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        max_s = 0
        while slow:
            max_s = max(max_s, prev.val + slow.val)
            prev = prev.next
            slow = slow.next
        
        return max_s