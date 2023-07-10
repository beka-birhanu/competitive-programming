# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # the whole idea is to split the list in to 2
        # and sum the twins 
        # twins are [1, 2, 3,   4, 5, 6]
        #                 <-i   i_t->

        
        fast, ith_twin = head, head

        ith = None
        while fast and fast.next:
            fast = fast.next.next
            tmp = ith_twin.next
            ith_twin.next = ith
            ith = ith_twin
            ith_twin = tmp
        
        max_sum = 0
        while ith_twin:
            max_sum = max(max_sum, ith.val + ith_twin.val)
            ith = ith.next
            ith_twin = ith_twin.next
        return max_sum
