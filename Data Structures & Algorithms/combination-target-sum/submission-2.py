class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or total > target:
                return
            curr.append(nums[i])
            backtrack(i, curr, total + nums[i])
            curr.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, curr, total)    
        backtrack(0, [], 0)
        return res        