# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        currMerge = dummy

        while list1 and list2:
            if list1.val < list2.val:
                currMerge.next = list1
                list1 = list1.next
            else:
                currMerge.next = list2
                list2 = list2.next
            currMerge = currMerge.next    

        if list1:
            currMerge.next = list1
        elif list2:
            currMerge.next = list2

        return dummy.next            
                 


