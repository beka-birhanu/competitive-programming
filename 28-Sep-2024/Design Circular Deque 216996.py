# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class LinkedNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularDeque:

    def __init__(self, k: int):
        self.max = k
        self.len = 0
        self.head = LinkedNode(-1)
        self.tail = LinkedNode(-1)
        self.tail.prev = self.head
        self.head.next = self.tail

    def insertFront(self, value: int) -> bool:
        if self.isFull(): return False
        second = self.head.next
        first = LinkedNode(value,self.head,second)
        self.head.next = first
        second.prev = first
        self.len += 1
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.isFull(): return False
        notlast = self.tail.prev
        last = LinkedNode(value,notlast,self.tail)
        self.tail.prev = last
        notlast.next = last
        self.len += 1
        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty(): return False
        a,b = self.head.next,self.head.next.next
        self.head.next = b
        b.prev = self.head
        self.len -= 1
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty(): return False
        b =self.tail.prev.prev
        self.tail.prev = b
        b.next = self.tail
        self.len -= 1
        return True

    def getFront(self) -> int: return self.head.next.val
        
    def getRear(self) -> int: return self.tail.prev.val

    def isEmpty(self) -> bool: return self.len==0

    def isFull(self) -> bool: return self.len==self.max




# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()