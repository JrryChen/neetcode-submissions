class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def solve(arr):
            n = len(arr)
            if n == 0: return 0
            prev2, prev1 = 0, 0
            for x in arr:
                prev2, prev1 = prev1, max(prev1, prev2 + x)
            return prev1
        
        return max(solve(nums[1:]), solve(nums[:-1]))