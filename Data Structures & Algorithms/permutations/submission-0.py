class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutation = []
        def backtrack(i):
            if i >= len(nums):
                res.append(permutation.copy())
                return
            for num in nums:
                if num in permutation:
                    continue
                permutation.append(num)
                backtrack(i + 1)
                permutation.pop()
        backtrack(0)
        return res                