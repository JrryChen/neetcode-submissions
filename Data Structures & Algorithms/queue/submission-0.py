class Node:
    def __init__(self, val, next_node = None, prev_node = None) -> None:
        self.val = val
        self.next = next_node
        self.prev = prev_node

class Deque:
    
    def __init__(self):
        self.head = Node(-1) # dummy head
        self.tail = self.head # pointer to last node

    def isEmpty(self) -> bool:
        return self.tail == self.head

    def append(self, value: int) -> None:
        self.tail.next = Node(value, None, self.tail)
        self.tail = self.tail.next

    def appendleft(self, value: int) -> None:
        new_node = Node(value, self.head.next, self.head)
        if self.head.next:
            self.head.next.prev = new_node
        else:
            self.tail = new_node
        self.head.next = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        res = self.tail

        self.tail = self.tail.prev
        self.tail.next = None
        return res.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        res = self.head.next
        self.head.next = res.next
        if self.head.next:
            self.head.next.prev = self.head
        else:
            self.tail = self.head
        return res.val    

