class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        optimized brute force
        '''
        mid = (len(nums1) + len(nums2)) / 2
        avg = not mid % 1
        target = int(mid) + 1
        print(target)
        ptr1, ptr2 = 0, 0
        val, prev = None, None
        while target > 0 and ptr1 < len(nums1) and ptr2 < len(nums2):
            prev = val
            if nums1[ptr1] <= nums2[ptr2]:
                val = nums1[ptr1]
                ptr1 += 1
            else:
                val = nums2[ptr2]
                ptr2 += 1
            target -= 1
            print(val, prev)

        while target > 0 and ptr1 < len(nums1):
            prev = val
            val = nums1[ptr1]
            target -= 1
            ptr1 += 1  

        while target > 0 and ptr2 < len(nums2):
            prev = val
            val = nums2[ptr2]
            target -= 1
            ptr2 += 1       

        return float(val) if not avg else (val + prev) / 2