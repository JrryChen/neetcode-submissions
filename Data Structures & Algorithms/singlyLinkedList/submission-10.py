class Node:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1) # dummy node
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while i < index and curr:
            i += 1
            curr = curr.next
        if not curr:
            return -1
        return curr.val    

    def insertHead(self, val: int) -> None:
        self.head.next = Node(val, self.head.next)
        if self.tail == self.head:
            self.tail = self.head.next

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        curr = self.head.next
        prev = self.head
        i = 0
        while i < index and curr:
            i += 1
            prev = curr
            curr = curr.next
            
        if not curr:
            return False

        prev.next = curr.next
        if curr == self.tail:
            self.tail = prev
        return True

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res    
