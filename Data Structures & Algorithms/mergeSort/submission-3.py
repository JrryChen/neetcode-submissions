# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if not pairs:
            return []

        def merge(arr, L, M, R): # similar to merging two linked lists!
            left_arr, right_arr = arr[L:M+1], arr[M+1:R+1] # create the left and right arrays
            left_ptr, right_ptr, ptr = 0, 0, L # indicies of l and r arr and then a global index for the actual array

            while left_ptr < len(left_arr) and right_ptr < len(right_arr): # Go through each element in the two arrays and combine
                if left_arr[left_ptr].key <= right_arr[right_ptr].key: # smaller entry is in the left
                    arr[ptr] = left_arr[left_ptr]
                    left_ptr += 1
                else: # smaller entry is in the right
                    arr[ptr] = right_arr[right_ptr]
                    right_ptr += 1
                ptr += 1
            # add the remaining elements in either array to the end
            while left_ptr < len(left_arr):
                arr[ptr] = left_arr[left_ptr]
                ptr += 1
                left_ptr += 1  
            while right_ptr < len(right_arr):
                arr[ptr] = right_arr[right_ptr]
                ptr += 1
                right_ptr += 1    
            return arr                

        def sort(arr, L, R):
            if L == R: # base case where we have 1 element
                return arr
            M = (L + R) // 2
            sort(arr, L, M) # sort the left array
            sort(arr, M+1, R) # sort the right arry   
            merge(arr, L, M, R) # merge the two arrays
            return arr
        return sort(pairs, 0, len(pairs) - 1)    