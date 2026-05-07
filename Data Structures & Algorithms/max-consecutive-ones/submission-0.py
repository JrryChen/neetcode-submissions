class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        res = 0
        streak = 0
        curr = 0
        while curr < n:
            if nums[curr] == 1:
                streak += 1
            else:
                res = max(res, streak)
                streak = 0
            curr += 1
        res = max(res, streak)    
        return res              