# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        before_left = None
        left_node = dummy
        for _ in range(left):
            before_left = left_node
            left_node = left_node.next 
        
        # revrese up until right
        right_node = left_node.next
        prev  =  left_node
        for _ in range(right - left):
            temp = right_node.next
            right_node.next, prev = prev, right_node
            right_node = temp
        
        left_node.next, before_left.next = right_node, prev

        return dummy.next 

        