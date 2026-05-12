class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        v_mid = -1
        while top <= bottom:
            v_mid = (top + bottom) // 2
            if matrix[v_mid][-1] < target:
                top = v_mid + 1
            elif matrix[v_mid][0] > target:
                bottom = v_mid - 1
            else:
                break
        if top > bottom:
            return False        
        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            h_mid = (left + right) // 2
            if matrix[v_mid][h_mid] == target:
                return True
            elif matrix[v_mid][h_mid] > target:
                right = h_mid - 1
            else:
                left = h_mid + 1
        print(matrix[v_mid][h_mid])
        return False               