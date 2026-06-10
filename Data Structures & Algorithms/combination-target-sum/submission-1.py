class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        subset = []
        def backtrack(i, subset, total):
            if total == target:
                output.append(subset.copy())
                return
            if i >= len(nums) or total > target:
                return
            subset.append(nums[i])
            backtrack(i, subset, total + nums[i])
            subset.pop()
            backtrack(i + 1, subset, total)
        backtrack(0, subset, 0)
        return output    