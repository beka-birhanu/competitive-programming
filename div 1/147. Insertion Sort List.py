# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Runtime 145ms and Memory 18.74MB

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(float("-inf"),head)
        prv = head
        curr = head.next

        while curr:
            if curr.val < prv.val:
                head = dummy
                while head.next.val < curr.val:
                    head = head.next
                to_be_inserted = curr
                curr = curr.next
                prv.next = curr
                head.next, to_be_inserted.next = to_be_inserted, head.next
            else:
                curr = curr.next
                prv = prv.next
    
        return dummy.next
