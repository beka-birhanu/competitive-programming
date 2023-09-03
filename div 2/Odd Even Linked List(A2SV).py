# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
            
        end_of_even = even_dummy = ListNode()
        odd_dummy = threshold = ListNode()

        ctr = 1
        while head:
            if ctr%2:
                threshold.next = head
                threshold = head
                head = head.next
                threshold.next = None

            else:
                end_of_even.next = head
                end_of_even = head
                head = head.next
                end_of_even.next = None
            ctr += 1


        threshold.next = even_dummy.next
        return odd_dummy.next
