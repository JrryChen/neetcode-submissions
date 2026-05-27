# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        '''
        general idea:
        choose a pivot point (often the last element in array)
        two pointers, one iterate through array, one keeps a swapping point
        if we get a value that is less than pivot point, we swap with the swapping point
        then we finish with a swap of the final element 
            and sort again between the two parts of the array
        '''

        if not pairs:
            return []

        def sort(arr, s, e):
            if s >= e:
                return arr
            pivot = arr[e]
            left = s  
            for i in range(s, e): # not e + 1 since we have pivot at e
                if arr[i].key < pivot.key:
                    arr[left], arr[i] = arr[i], arr[left]
                    left += 1
            arr[e], arr[left] = arr[left], arr[e]
            sort(arr, s, left - 1)
            sort(arr, left + 1, e)
            return arr

        return sort(pairs, 0, len(pairs) - 1)            