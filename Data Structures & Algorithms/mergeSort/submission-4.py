# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if not pairs:
            return []

        def merge(arr, L, M, R):
            left_arr, right_arr = arr[L:M+1], arr[M+1:R+1]
            l_ptr, r_ptr, ptr = 0, 0, L
            while l_ptr < len(left_arr) and r_ptr < len(right_arr):
                if left_arr[l_ptr].key <= right_arr[r_ptr].key:
                    arr[ptr] = left_arr[l_ptr]
                    l_ptr += 1
                else:
                    arr[ptr] = right_arr[r_ptr]
                    r_ptr += 1    
                ptr += 1
            while l_ptr < len(left_arr):
                arr[ptr] = left_arr[l_ptr]
                l_ptr += 1
                ptr += 1
            while r_ptr < len(right_arr):
                arr[ptr] = right_arr[r_ptr]
                r_ptr += 1
                ptr += 1  
            return arr

        def sort(arr, L, R):
            if L == R:
                return arr
            M = (L + R) // 2
            sort(arr, L, M)
            sort(arr, M+1, R)
            merge(arr, L, M, R)
            return arr 
        return sort(pairs, 0, len(pairs) - 1)           