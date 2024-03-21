# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev = None
        curr = head

        # link the nodes backwards 
        while curr:
            prev, curr.prev, curr = curr, prev, curr.next
             
        right = prev
        left = head

        while left != right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.prev

        return True