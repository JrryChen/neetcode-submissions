# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        dictionary to keep track of curr_nodes
        as we insert the min element, once we hit the end of a list, delete from dictionary
        continue while dictionary 
        '''
        curr_nodes = {} # index : pointer
        head = ListNode(-1)
        curr = head

        for i, node in enumerate(lists):
            curr_nodes[i] = node

        while curr_nodes:
            min_node = None
            min_key = -1
            for i in curr_nodes.keys():
                if not min_node:
                    min_node = curr_nodes[i]
                    min_key = i
                    continue
                if min_node.val > curr_nodes[i].val:
                    min_node = curr_nodes[i]
                    min_key = i
            curr.next = min_node
            curr = curr.next
            curr_nodes[min_key] = curr_nodes[min_key].next
            if not curr_nodes[min_key]:
                del curr_nodes[min_key] 

        return head.next    


