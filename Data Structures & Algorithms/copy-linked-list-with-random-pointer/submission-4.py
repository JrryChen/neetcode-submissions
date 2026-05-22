"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        mp = {}
        curr = head
        prev = None
        res_head = None
        while curr:
            mp[curr] = Node(curr.val)
            if prev:
                prev.next = mp[curr]
            if curr == head:
                res_head = mp[curr] 
            prev = mp[curr]
            curr = curr.next

        for n in mp.keys():
            copy = mp[n]
            copy.random = mp[n.random] if n.random else None    

        return res_head    
