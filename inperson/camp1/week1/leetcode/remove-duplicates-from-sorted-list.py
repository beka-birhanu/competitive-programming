# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        left = head
        right = head

        while left:
            while right and right.val == left.val:
                right = right.next
            left.next = right
            left = left.next
        
        return head
