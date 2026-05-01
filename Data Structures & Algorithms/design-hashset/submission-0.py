class ListNode:
    def __init__(self, key) -> None:
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.mem = [ListNode(-1) for i in range(10**4)]  # dummy nodes
        
    def add(self, key: int) -> None:
        curr = self.mem[key % len(self.mem)]
        while curr.next:
            if curr.next.key == key:
                return
            curr = curr.next
        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        curr = self.mem[key % len(self.mem)]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        

    def contains(self, key: int) -> bool:
        curr = self.mem[key % len(self.mem)]
        while curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)