# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head:
            prv = dum_head = head
            while dum_head and dum_head.val < x:
                prv = dum_head
                dum_head = dum_head.next
            dum_head = prv
            curr = dum_head
            while curr.next:
                prv = curr
                curr = curr.next
                if curr.val < x:
                    prv. next = curr.next
                    if dum_head.val < x:
                        curr.next = dum_head.next
                        dum_head.next = curr
                        dum_head = curr
                    else:
                        curr.next = dum_head
                        dum_head = head = curr
                        curr = prv
        return head
