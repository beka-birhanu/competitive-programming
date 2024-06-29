# Problem: LFU Cache - https://leetcode.com/problems/lfu-cache/

from collections import defaultdict

class LinkedNode:
    def __init__(self, val:int, key: int, prev=None, next=None):
        self.val = val
        self.key = key
        self.freq = 1
        self.prev = prev
        self.next = next

class CircularDeque:

    def __init__(self):
        self.len = 0
        self.head = LinkedNode(-1, -1)
        self.tail = LinkedNode(-1, -1)
        self.tail.prev = self.head
        self.head.next = self.tail        

    def append(self, value: int, key: int) -> LinkedNode:
        notlast = self.tail.prev
        last = LinkedNode(value, key, notlast, self.tail)
        self.tail.prev = last
        notlast.next = last
        self.len += 1
        return last

    def remove(self, node: LinkedNode) -> None:
        self.len -= 1
        prev_node = node.prev
        prev_node.next = node.next
        node.next.prev = prev_node

    def popleft(self) -> LinkedNode:
        if self.isEmpty(): 
            return None
        first = self.head.next
        self.remove(first)
        return first
        
    def isEmpty(self) -> bool: 
        return self.len == 0

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.min_freq = 1
        self.freq_bucket = defaultdict(lambda: CircularDeque())

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._update(node)
        return node.val
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._update(node)
        
        else:
            if len(self.cache) >= self.capacity:
                bucket = self.freq_bucket[self.min_freq]
                least_used = bucket.popleft()
                del self.cache[least_used.key]

            node = self.freq_bucket[1].append(value, key)
            self.cache[key] = node
            self.min_freq = 1

    def _update(self, node: LinkedNode):
        bucket = self.freq_bucket[node.freq]
        bucket.remove(node)

        if bucket.len == 0 and self.min_freq == node.freq:
            self.min_freq += 1

        new_bucket = self.freq_bucket[node.freq + 1]
        new_node = new_bucket.append(node.val, node.key)
        new_node.freq += node.freq

        self.cache[node.key] = new_node
