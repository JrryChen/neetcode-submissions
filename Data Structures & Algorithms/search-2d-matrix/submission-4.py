class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            mid_row = (bottom + top) // 2
            if target < matrix[mid_row][0]:
                bottom = mid_row - 1
            elif target > matrix[mid_row][-1]:
                top = mid_row + 1
            else:
                break 
        if top > bottom:
            return False

        row = (bottom + top) // 2
        left, right = 0, len(matrix[row]) - 1
        while left <= right:
            mid_col = (left + right) // 2
            if target < matrix[row][mid_col]:
                right = mid_col - 1
            elif target > matrix[row][mid_col]:
                left = mid_col + 1
            else:
                return True
        return False        
                    



