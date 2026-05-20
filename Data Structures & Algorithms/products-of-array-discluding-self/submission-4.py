class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = 0
        cumprod = 1
        for num in nums:
            if num == 0:
                zeroCount += 1
            else:
                cumprod *= num

        res = [0] * len(nums)
        if zeroCount > 1:
            return res

        for i in range(len(nums)):
            if zeroCount == 1:
                if nums[i] == 0:
                    res[i] = cumprod
                    return res
                else:
                    continue    
            res[i] = cumprod // nums[i]       

        return res