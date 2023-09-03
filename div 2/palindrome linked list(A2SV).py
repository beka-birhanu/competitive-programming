# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        st_num = ""
        while head:
            st_num += str(head.val)
            head = head.next
        for i in range(len(st_num)//2 + 1):
            if st_num[i] != st_num[-1-i]:
                return False
        return True
