class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]: # the left side of array is sorted
                if nums[left] <= target < nums[mid]: # target is in on the left side
                    right = mid - 1
                else: # target is less than nums[left] or more than nums[mid], either way its on the right side
                    left = mid + 1
            else: # nums[left] > nums[mid] => pivot point is in left side
                if nums[mid] < target < nums[left]: #target is in the right side (values between nums[mid] and nums[left])
                    left = mid + 1
                else:
                    right = mid - 1    

        return -1