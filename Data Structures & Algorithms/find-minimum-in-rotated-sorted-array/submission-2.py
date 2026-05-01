class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        binary search
        get the mid point
           if nums[mid] > nums[0]:
                res is going to be on the right
            if less, is going to be on the left

            **edge cases:
                eaxmple 2: mid is the min => we search on the right, no values will be less than the mid so we return that once while lop completes
                example 3: if min is the first element => we search the right side until we don't find a number smaller than n[0]    
                to deal wit this, we get the min between the first and mid element, keep trakc of this min since it wont change
        '''
        res = nums[0]
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])

            mid = left + ((right - left) // 2)
            res = min(res, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        return res            