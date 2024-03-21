
class Node:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int, want_val = True) -> int:
        if index >= self.size:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next

        return curr.val if want_val else curr

    def addAtHead(self, val: int) -> None:
        if self.size:
            new_head = Node(val,self.head)
            self.head = new_head

        else:
            new_head = Node(val)
            self.head = new_head
            self.tail = new_head

        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.size:
            new_tail = Node(val)
            self.tail.next, self.tail = new_tail, new_tail

        else:
            new_tail= Node(val)
            self.head = new_tail
            self.tail = new_tail
            
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return 
        
        if index == self.size:
            return self.addAtTail(val)
        
        if index == 0:
            return self.addAtHead(val)
        
        new_node = Node(val)
        curr = self.get(index-1, False)
        
        new_node.next, curr.next = curr.next, new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return

        if self.size == 1:
            self.head = None
            self.tail = None
            
        elif index == 0:
            self.head = self.head.next
        
        elif index == self.size-1:
            new_tail = self.get(index-1, False)
            self.tail, new_tail.next = new_tail, None
        else:
            curr = self.get(index-1, False)
            curr.next = curr.next.next

        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)