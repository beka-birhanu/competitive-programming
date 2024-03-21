class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val 
        self.prev = prev
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.max_size = k
        self.size = 0
        self.head  = ListNode()
        self.head.next = self.head.prev = self.head #connect head to itself 

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        end = self.head.prev
        new_node = ListNode(value, end, self.head)
        
        end.next = new_node
        self.head.prev = new_node
        
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False 

        start = self.head.next
        start.next.prev, self.head.next = self.head, start.next

        del start
        self.size -= 1
        
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.head.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.head.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0      

    def isFull(self) -> bool:
        return self.size == self.max_size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()