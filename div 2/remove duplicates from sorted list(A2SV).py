# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dem_head = head
        while dem_head and dem_head.next:
            cur = dem_head
            while cur and dem_head.val == cur.val:
                cur = cur.next
                dem_head.next = cur
            dem_head = dem_head.next
        return head
