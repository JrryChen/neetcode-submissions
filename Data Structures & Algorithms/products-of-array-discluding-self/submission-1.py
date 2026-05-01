class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # BruteForce
        # n = len(nums)
        # res = [0]* n
        # for i in range(n):
        #     prod = 1
        #     for j in range(n):
        #         if i == j:
        #             continue
        #         prod *= nums[j] 
        #     res[i] = prod
        # return res   
        res = [0] * len(nums)
        prod = 1
        zeroCount = 0
        for num in nums:
            if num == 0:
                zeroCount += 1
            else:
                prod *= num
        if zeroCount > 1:
            return res

        for i, number in enumerate(nums):
            if zeroCount: 
                res[i] = 0 if number else prod
            else:
                res[i] = prod // number
        return res                    