class Node:
    def __init__(self, key, value):
        self.key, self.val = key, value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hp = {} #map key to node

        self.least, self.most = Node(0, 0), Node(0, 0)
        self.least.next, self.most.prev = self.most, self.least

    def remove(self, node):
        # node.prev.next = node.next
        # node.next.prev = node.prev
        # node.next = None
        # node.prev = None
        # This doesn't work due to pointers changing, need to use var like below to maintain correct pointers
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def add(self, node):   #insert at right    
        prev = self.most.prev
        prev.next = node
        self.most.prev = node
        node.next = self.most
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.hp:
            self.remove(self.hp[key])
            self.add(self.hp[key])
            return self.hp[key].val
        return -1    
        

    def put(self, key: int, value: int) -> None:
        if key in self.hp:
            self.remove(self.hp[key])
        self.hp[key] = Node(key, value)
        self.add(self.hp[key])

        if len(self.hp) > self.capacity:
            lru = self.least.next
            self.remove(lru)
            del self.hp[lru.key]

        
