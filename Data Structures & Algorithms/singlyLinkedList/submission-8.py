class Node:
    def __init__(self, val: int, next_node = None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head
        for i in range(index + 1):
            curr = curr.next
            if curr == None:
                return -1
        return curr.val        

    def insertHead(self, val: int) -> None:
        self.head.next = Node(val, self.head.next)
        if not self.head.next.next:
            self.tail = self.head.next

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        curr = self.head.next
        prev = self.head
        i = 0
        while i < index and curr:
            prev = curr
            curr = curr.next
            i += 1
        if curr:
            if curr == self.tail:
                self.tail = prev
                prev.next = None
            else:
                prev.next = curr.next
            return True
        return False    

    def getValues(self) -> List[int]:
        res = []
        curr = self.head
        while curr.next:
            curr = curr.next
            res.append(curr.val)
        return res    
