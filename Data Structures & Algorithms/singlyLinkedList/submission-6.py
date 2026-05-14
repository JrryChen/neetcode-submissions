class Node:
    def __init__(self, val, next_node = None):
        self.next = next_node
        self.val = val

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.count = 0
    
    def get(self, index: int) -> int:
        if index >= self.count:
            return -1
        curr_node = self.head
        curr = 0
        while curr < index:
            curr += 1
            curr_node = curr_node.next
        return curr_node.val        
    def insertHead(self, val: int) -> None:
        self.head = Node(val, next_node = self.head)
        self.count += 1

    def insertTail(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
            self.count += 1
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(val)
            self.count += 1    

    def remove(self, index: int) -> bool:
        if index >= self.count:
            return False
        if index == 0:
            self.head = self.head.next   
            self.count -= 1
            return True 
        curr = 0
        curr_node = self.head
        prev_node = None
        while curr < index:
            curr += 1
            prev_node = curr_node
            curr_node = curr_node.next
        if self.count == 1:
            self.head = None
            return True    
        prev_node.next = curr_node.next
        self.count -= 1
        return True    

    def getValues(self) -> List[int]:
        res = []
        curr = self.head
        while curr is not None:
            res.append(curr.val)
            curr = curr.next
        return res    
