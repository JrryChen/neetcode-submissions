class Node:
    def __init__(self, key, val, next_node = None, prev_node = None):
        self.key = key
        self.val = val
        self.next = next_node
        self.prev = prev_node

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = {} # key : Node
        # Nodes closer to head is least recenlty used
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.values:
            self.remove(self.values[key])
            self.insert(self.values[key])
            return self.values[key].val
        return -1    

    def put(self, key: int, value: int) -> None:
        if key in self.values:
            self.values[key].val = value
            self.remove(self.values[key])
            self.insert(self.values[key])
        else:
            self.values[key] = Node(key, value)
            self.insert(self.values[key])
            if len(self.values) > self.capacity:
                lru = self.head.next
                self.remove(lru)
                del self.values[lru.key]


    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        prev, nex = self.tail.prev, self.tail
        node.prev = prev
        node.next = nex
        node.prev.next = node
        node.next.prev = node
