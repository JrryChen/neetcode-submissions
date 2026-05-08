class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = 0
        prod = 1

        for n in nums:
            if n == 0:
                zeroCount += 1
            else:
                prod *= n

        res = [0] * len(nums)
        if zeroCount > 1:
            return res

        for i, n in enumerate(nums):
            if zeroCount:
                if n == 0:
                    res[i] = prod
            else:
                res[i] = prod // n

        return res                             