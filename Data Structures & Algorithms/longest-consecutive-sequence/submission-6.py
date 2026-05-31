class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        for num in nums:
            length = 1
            while (num + length) in nums:
                length += 1
            res = max(res, length)
        return res        