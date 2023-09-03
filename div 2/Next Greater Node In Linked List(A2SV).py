# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        list_val = deque()
        while head:
            list_val.appendleft(head.val)
            head = head.next

        n = len(list_val)
        ans = [0]*n

        monoton_stack = []
        for idx, val in enumerate(list_val):
            while monoton_stack and monoton_stack[-1] <= val:
                monoton_stack.pop()
            
            if len(monoton_stack ):
                ans[n-idx-1] = monoton_stack[-1]
            monoton_stack.append(val)
        return ans
