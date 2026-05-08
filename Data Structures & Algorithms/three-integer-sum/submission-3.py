class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if nums[i] > 0: #we can't get any smaller so theres no solution
                break
            a = nums[i]
            if i > 0 and a == nums[i - 1]:
                continue 
            left, right = i + 1, len(nums) - 1
            while left < right:
                threeSum = nums[left] + nums[right] + a

                if threeSum == 0:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif threeSum > 0:
                    right -= 1
                else:
                    left += 1


        return res        
