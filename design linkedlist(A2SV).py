class Node():
    def __init__(self,data = None) -> None:
        self.data = data
        self.next = None
        self.prvious = None 

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = -1

    def get(self, index: int) -> int:
        if index > self.size:
            return -1

        elif self.head:
            curr = self.head
            for i in range(1,index+1):
                curr = curr.next 
            return curr.data

    def addAtHead(self, val: int) -> None:
        to_be = Node(val)
        if not self.head:
            self.head = self.tail = to_be

        else:
            self.head.prvious = to_be
            to_be.next = self.head
            self.head = to_be
        self.size += 1

    def addAtTail(self, val: int) -> None:
        to_be = Node(val)
        if not self.head:
            self.head = self.tail = to_be

        else:
            self.tail.next = to_be
            to_be.prvious = self.tail
            self.tail = to_be

        self.size += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        to_be = Node(val)
        if index > self.size + 1:
            return
        else:
            if index == self.size + 1:
                self.addAtTail(val)
                self.size -= 1

            elif  index == 0:
                self.addAtHead(val)
                self.size -= 1
            else:
                curr = self.head

                for i in range(1,index):
                    curr = curr.next 

                to_be.next = curr.next
                curr.next.prvious = to_be
                curr.next = to_be
                to_be.prvious = curr
            self.size += 1
    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        if index  > self.size:
            return
        if 0 == index:
            self.head = curr.next

        elif index == self.size:
            self.tail = self.tail.prvious
        else:
            for i in range(1,index+1):
                curr = curr.next                
                if i == index:
                    curr.prvious.next = curr.next
                    curr.next.prvious = curr.prvious
        self.size -= 1
