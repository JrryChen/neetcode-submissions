class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        seen = set()
        
        for i in range(len(nums)):
            if nums[i] > 0: # every number from index i and on is positive, so its imposisble for any new combinations to be 0
                break 
            a = nums[i]
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
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1       
                     
        return res                    

        