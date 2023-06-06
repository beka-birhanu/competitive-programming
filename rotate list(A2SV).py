# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def tailHead(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = prv = head

        while cur.next:
            prv = cur
            cur = cur.next

        if prv != cur:
            prv.next = None
            cur.next = head
            
        return cur

        
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        size = 1
        while cur and cur.next:
            size +=1
            cur  = cur.next
        k = k % size
        for _ in range(k):
            head = self.tailHead(head)
        return head
