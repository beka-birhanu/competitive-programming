# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        end_of_even = even_dummy = ListNode()
        odd_dummy = threshold = ListNode()

        ctr = 1
        curr = head
        while curr:
            if ctr%2:
                threshold.next = curr
                threshold = threshold.next
                curr = curr.next

            else:
                end_of_even.next = curr
                end_of_even = end_of_even.next
                curr = curr.next

            ctr += 1


        threshold.next = even_dummy.next
        end_of_even.next = None
        return odd_dummy.next