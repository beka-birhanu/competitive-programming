# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            curr.next = minm =None
            if list1.val > list2.val:
                minm = list2
                list2 = list2.next
            else:
                minm = list1
                list1 = list1.next
            
            curr.next = minm
            curr = curr.next
        while list1:
            curr.next = list1
            curr = curr.next
            list1 = list1.next

        while list2:
            curr.next = list2
            curr = curr.next
            list2 = list2.next
        
        curr.next = None

        return dummy.next
