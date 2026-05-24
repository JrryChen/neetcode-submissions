# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None

        curr1, curr2 = l1, l2
        res = ListNode(-1)
        curr = res
        carry = 0

        while curr1 and curr2:
            val = curr1.val + curr2.val + carry
            if val >= 10:
                carry = 1
                val = val % 10
            else:
                carry = 0
            curr.next = ListNode(val)
            curr = curr.next
            curr1 = curr1.next
            curr2 = curr2.next

        while curr1:
            val = curr1.val + carry
            if val >= 10:
                carry = 1
                val = val % 10
            else:
                carry = 0
            curr.next = ListNode(val)
            curr = curr.next
            curr1 = curr1.next

        while curr2:
            val = curr2.val + carry
            if val >= 10:
                carry = 1
                val = val % 10
            else:
                carry = 0
            curr.next = ListNode(val)
            curr = curr.next  
            curr2 = curr2.next

        if carry:
            curr.next = ListNode(1)

        return res.next
