class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        2 pointers and move the pointer dpeneding if the sum is greater or smaller than target
        move right pointer left to make sum smaller and left point right to make sum bigger
        '''

        l, r = 0, len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total > target:
                r -= 1
            elif total < target:
                l += 1
            else:
                return [l + 1, r + 1]        