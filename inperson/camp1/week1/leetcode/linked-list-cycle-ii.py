# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head 
       
        # check if a cycle exists
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        
        else: #if no cycle
            return
        
        #if there is a cycle find the cycle enterace by making the fast move as fast as the slow one 
        fast = head
        while True:
            if slow == fast:
                return slow
            fast = fast.next
            slow = slow.next
            
        
        