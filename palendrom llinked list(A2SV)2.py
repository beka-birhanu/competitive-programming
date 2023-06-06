# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # st_num = ""
    # while head:
    #     st_num += str(head.val)
    #     head = head.next
    # for i in range(len(st_num)//2 + 1):
    #     if st_num[i] != st_num[-1-i]:
    #         return False
    # return True

    # no need for creating list and taking more space 
    # divide the list in half
    # and simple check if they are same 
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        dem_head = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = dem_head
            dem_head = curr
            curr = next_node
        
        while dem_head:
            if head.val != dem_head.val:
                return False
            head = head.next
            dem_head = dem_head.next
        
        return True
