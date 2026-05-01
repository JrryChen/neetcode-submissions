class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hp = defaultdict(Node) #key : Node
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hp:
            return -1
        node = self.hp[key]
        self.remove(node)
        self.add(node)
        return node.value    

    def put(self, key: int, value: int) -> None:
        if key in self.hp:
           self.remove(self.hp[key])
        new_node = Node(key, value)
        self.hp[key] = new_node
        self.add(new_node)
        if len(self.hp) > self.capacity:
            remove_node = self.head.next
            self.remove(self.head.next)
            del self.hp[remove_node.key]


    def add(self, node): #adds to the end of the linked list
        end = self.tail.prev
        end.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = end
        
    def remove(self, node): #removes a node from the linked list
        node.prev.next = node.next
        node.next.prev = node.prev    
        
