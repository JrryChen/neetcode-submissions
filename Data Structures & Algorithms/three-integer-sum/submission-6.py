class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        sort nums
        use a set to prevent duplicate triplets
        iterate through nums and basically run 2sum
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
            left, right = i + 1, len(nums) - 1
            while left < right:
                cumsum = nums[left] + nums[right] + a
                if cumsum > 0:
                    right -= 1
                elif cumsum < 0:
                    left += 1
                else:
                    res.append([nums[left], nums[right], a])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return res                    
        