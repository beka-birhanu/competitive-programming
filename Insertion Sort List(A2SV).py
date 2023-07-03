# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(float("-inf"),head)
        prv = head
        curr = head.next

        while curr:
            to_be_inserted =  curr
            curr = curr.next
            prv.next = curr
            start = dummy
    
            while (start and start.next) and  (to_be_inserted.val >= start.next.val) and (start != prv):
            
                start = start.next
            to_be_inserted.next = start.next
            start.next = to_be_inserted
            if prv.next != curr:
                prv = prv.next
        return dummy.next
