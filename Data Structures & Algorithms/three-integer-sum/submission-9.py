class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        sort the nums List
        iterate through each and find if there are any valid triplets using 2sum (2 pointers)
            increment left +1 and right -1
            increment left +1 while we have the same left number
        '''

        nums.sort()
        res = []
        seen = set()

        for i in range(len(nums)):
            a = nums[i]
            if a > 0:
                break
            if a in seen:
                continue
            seen.add(a)    
            l, r = i + 1, len(nums) - 1
            while l < r:
                cumsum = a + nums[l] + nums[r]
                if cumsum > 0:
                    r -= 1
                elif cumsum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1        
        return res        