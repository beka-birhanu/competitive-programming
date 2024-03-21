# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-5001,head)
        sorted_last = dummy #last node of the sorted portion
        curr = dummy

        while curr: #to iterate until this reaches the endor serves like for i in range(len(list))
            if curr.val < sorted_last.val:
                #find the right prev for the current node
                prev = dummy
                while prev.next.val < curr.val:
                    prev = prev.next

                sorted_last.next = curr.next
                curr.next, prev.next= prev.next, curr
            else:
                sorted_last = sorted_last.next

            curr = sorted_last.next
        return dummy.next