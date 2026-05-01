class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in differences:
                return [differences[diff], i]
            differences[num] = i    
