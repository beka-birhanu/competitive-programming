# Runtime 93ms and Memory20Mb


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for l,node in enumerate(lists):
            if node:
                heapq.heappush(heap,[node.val,l])
                

        merged = ListNode()
        curr = merged
        while heap:
            val,l = heapq.heappop(heap)
            curr.next = lists[l] 
            curr = curr.next
            if lists[l].next:
                lists[l] = lists[l].next
                heapq.heappush(heap,[lists[l].val,l])
                
        return merged.next
