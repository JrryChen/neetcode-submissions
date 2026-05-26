# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        '''
        divide the array into two parts and sort the two parts
        basecase: we have array of 1 (sorted)
        merge the two arrays in a sorted fashion
        '''
        if not pairs:
            return []
        def merge(arr, L, M, R):
            l_arr, r_arr = arr[L:M+1], arr[M+1:R+1]
            l, r, ptr = 0, 0, L
            while l < len(l_arr) and r < len(r_arr):
                if l_arr[l].key <= r_arr[r].key:
                    arr[ptr] = l_arr[l]
                    l += 1
                else:
                    arr[ptr] = r_arr[r]
                    r += 1
                ptr += 1

            while l < len(l_arr):
                arr[ptr] = l_arr[l]
                l += 1 
                ptr += 1

            while r < len(r_arr):
                arr[ptr] = r_arr[r]
                r += 1 
                ptr += 1         
            return arr
        def sort(arr, L, R): 
            if L == R:
                return arr
            M = (L + R) // 2                
            sort(arr, L, M)
            sort(arr, M + 1, R)
            merge(arr, L, M, R)
            return arr     
        return sort(pairs, 0, len(pairs) - 1)