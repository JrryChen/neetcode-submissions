class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        compare = len(nums) - k
        def select(arr, s, e):
            while s <= e:
                # Select middle as pivot and swap to end to avoid O(n^2) on sorted/identical arrays
                mid = (s + e) // 2
                arr[mid], arr[e] = arr[e], arr[mid]
                
                pivot = arr[e]
                left = s
                for i in range(s, e):
                    if arr[i] < pivot:
                        arr[i], arr[left] = arr[left], arr[i]
                        left += 1
                arr[e], arr[left] = arr[left], arr[e]
                
                if compare == left:
                    return arr[left]
                elif compare < left:
                    e = left - 1
                else:
                    s = left + 1
        return select(nums, 0, len(nums) - 1)