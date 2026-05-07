class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        zeroCount, prod = 0, 1
        for num in nums:
            if num == 0:
                zeroCount +=1
            else:
                prod *= num

        if zeroCount > 1:
            return res

        for i, number in enumerate(nums):
            if zeroCount:
                if number == 0:
                    res[i] = prod
                    return res
            else:
                res[i] = prod // number

        return res                