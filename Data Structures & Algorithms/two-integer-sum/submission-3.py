class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in differences:
                return [differences[diff], i]
            differences[nums[i]] = i