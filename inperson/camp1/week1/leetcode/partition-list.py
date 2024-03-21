# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(x-1,head)
        ptr = dummy #to iterate until this reaches the endor serves like for i in range(len(list))
        while ptr:
            curr = dummy
            nxt = head
            while nxt:
                if nxt.val < x and curr.val >= x:
                    nxt.val, curr.val = curr.val, nxt.val
                    
                nxt = nxt.next
                curr =  curr.next
            
            ptr = ptr.next

        return dummy.next
                    