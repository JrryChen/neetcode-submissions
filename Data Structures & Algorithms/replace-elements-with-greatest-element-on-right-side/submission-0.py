class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0] * n
        top = -1
        for i in range(n-1, -1, -1):
            res[i] = top
            top = max(top, arr[i])

        return res    