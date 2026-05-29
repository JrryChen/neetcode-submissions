# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        merge sort but on linked lists
        '''
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedList.append(self.merge(l1, l2))
            lists = mergedList
        return lists[0]        
                   


    def merge(self, node1, node2):
        head = ListNode(-1)
        curr = head
        while node1 and node2:
            if node1.val < node2.val:
                curr.next = node1
                node1 = node1.next
            else:
                curr.next = node2
                node2 = node2.next
            curr = curr.next
        while node1:
            curr.next = node1
            node1 = node1.next
            curr = curr.next 
        while node2:
            curr.next = node2
            node2 = node2.next
            curr = curr.next
        return head.next    



