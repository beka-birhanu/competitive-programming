# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dem_head = ListNode(0,head)
        prv = dem_head 

        while head:
            if head.next and head.val ==  head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prv.next = head.next
            
            else:
                prv  = prv.next
            head = head.next
        

        return dem_head.next
