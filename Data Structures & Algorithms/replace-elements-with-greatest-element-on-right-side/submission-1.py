class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        top = -1
        for i in range(n-1, -1, -1):
            prev = arr[i]
            arr[i] = top
            top = max(top, prev)

        return arr   