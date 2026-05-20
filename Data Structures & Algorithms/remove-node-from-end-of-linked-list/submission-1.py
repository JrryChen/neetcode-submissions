# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        remove = tail = head
        prev = None
        for i in range(n):
            tail = tail.next

        while tail:
            prev = remove
            remove = remove.next
            tail = tail.next
        if remove == head:
            return remove.next
        prev.next = remove.next    
        return head    

