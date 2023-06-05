# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left < right:
            if left > 1:
                cur = head 
                for _ in range(1,left-1):
                    cur = cur.next
                left_untouched = cur
                print(left_untouched.val)

                for _ in range(left-1, right+1):
                    cur = cur.next
                right_untouched = cur

                dem_head = right_untouched
                cur = left_untouched.next
                while cur.next and cur.next != right_untouched:
                    prv = cur
                    cur = cur.next
                    prv.next = dem_head
                    dem_head = prv
                cur.next = dem_head
                left_untouched.next = cur
            else:
                cur = head
                for _ in range(left, right+1):
                    cur = cur.next
                right_untouched = cur

                dem_head = right_untouched
                cur = head
                while cur.next and cur.next != right_untouched:
                    prv = cur
                    cur = cur.next
                    prv.next = dem_head
                    dem_head = prv
                cur.next = dem_head
                head = cur
                
        return head
