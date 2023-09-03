# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        dummy.next = head
        slow = head
        while head and head.next:
            head =  head.next.next
            slow = slow.next

            if head == slow:
                slow =  dummy.next
                while slow != head:
                    slow = slow.next
                    head = head.next
                return slow
