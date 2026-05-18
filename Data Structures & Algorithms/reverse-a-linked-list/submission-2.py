# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        maintain pointer to prev node and current node
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        
        stop when curr.next is null and return curr
        '''
        if not head:
            return None
        curr = head
        prev = None
        while curr.next:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        curr.next = prev
        return curr    