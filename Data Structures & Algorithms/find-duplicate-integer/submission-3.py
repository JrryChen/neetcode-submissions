class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        model each value in nums as a pointer to an index
        [1, 2, 3, 2, 2] 
            index 0 points to 1
            index 1 goes to 2
            index 2 goes to 3
            index 3 goes to 2
        This creates a graph and we can use floyd's algorithm to check for cycle
        '''
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                break
        return slow                
