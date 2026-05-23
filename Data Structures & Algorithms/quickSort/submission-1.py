# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        if not pairs:
            return []

        def sort(arr, s, e):
            if s >= e:
                return arr
            pivot = arr[e]
            left = s
            for i in range(s, e):
                if arr[i].key < pivot.key:
                    arr[i], arr[left] = arr[left], arr[i]
                    left += 1

            arr[left], arr[e] = arr[e], arr[left]
            sort(arr, s, left-1)
            sort(arr, left+1, e)
            return arr

        return sort(pairs, 0, len(pairs) - 1)            