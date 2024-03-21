# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        def find_length (head:Optional[ListNode]) -> int:
            curr = head
            length = 0

            while curr:
                length += 1
                curr = curr.next
            return length
        
        
        def disconnect_parts(parts:List[Optional[ListNode]]) -> None:
             #disconnect the parts
            for i in range(len(parts)-1):
                curr = parts[i]
                next_part_head = parts[i+1]

                if not curr:
                    break

                while curr and curr.next != next_part_head:
                    curr = curr.next

                curr.next = None

        length = find_length(head)
        parts = [head]
        size = length//k

        # first divide the partitions assuming all parts are of equal length
        for _ in range(1,k):
            part_head = parts[-1]
            for gap in range(size):
                if part_head:
                    part_head = part_head.next
                else:
                    break

            parts.append(part_head)
        #then acoomoodet for cases the parts are not equal
        r = length % k 
        moves = 0 #the number of moves the head starting form the second part has to move due to the shift of the previous head
        for i in range(1,len(parts)):
            my_moves = moves + (1 if r>0 else 0)
            part_head = parts[i]
            if not part_head:
                break

            while part_head and my_moves:
                part_head = part_head.next
                my_moves -= 1
            
            parts[i] = part_head
            moves += (1 if r > 0 else 0)
            r -= 1

        disconnect_parts(parts)

        return parts