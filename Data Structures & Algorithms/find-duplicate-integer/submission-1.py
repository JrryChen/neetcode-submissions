class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        Linked List Cycle detection with slow and fast pointer
        Floyd's algorithm
            - Slow + Fast pointer until they intersect.
            - Keep one slow pointer at the intersect and one at the start
            - iterate slow pointers until they interset = cycle start
        Inutition => the intersection point of slow/fast pointer 
            will be the same distance from cycle start from the initial start
        '''
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow1 = 0
        while True:
            slow = nums[slow]
            slow1 = nums[slow1]
            if slow == slow1:
                break
        return slow                