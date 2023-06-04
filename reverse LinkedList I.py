# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            dem_head = None
            while head.next:
                prv = head
                head = head.next
                prv.next = dem_head
                dem_head = prv
            head.next = dem_head
            return head
