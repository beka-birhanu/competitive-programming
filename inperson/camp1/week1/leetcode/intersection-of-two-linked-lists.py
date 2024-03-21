# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curr = headA
        while curr:
            curr.val = -curr.val
            curr = curr.next

        start = None
        curr = headB
        while curr:
            if curr.val < 0:
                if not start:
                    start = curr
                curr.val = -curr.val
            curr = curr.next

        curr = headA
        while curr:
            if curr.val > 0:
                break
            
            curr.val = -curr.val
            curr = curr.next

        return start