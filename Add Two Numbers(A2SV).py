# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr_digit = dummy
        r  = 0
        while l1 or l2:
            if l1 and l2:
                digit_sum = l1.val + l2.val + r
                l1 =  l1.next
                l2 = l2.next
            elif l1:
                digit_sum = l1.val + r
                l1 =  l1.next
            else:
                digit_sum = l2.val + r
                l2 = l2.next


            r = digit_sum // 10
            curr_digit.next = ListNode(digit_sum % 10)

            curr_digit = curr_digit.next

        if r :
            curr_digit.next = ListNode(r)
        return dummy.next
