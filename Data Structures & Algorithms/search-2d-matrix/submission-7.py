class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        matrix is sorted so we can binary search
        binary search on rows then binary search on col in the rows
        '''
        m, n = len(matrix), len(matrix[0])

        # binary search for row
        top, bottom = 0, m - 1
        target_row = -1
        while top <= bottom:
            row = (top + bottom) // 2
            if matrix[row][0] > target: #smallest value in row is still bigger so we need to search above
                bottom = row - 1
            elif matrix[row][n - 1] < target: #largest in row is smaller than target so we need to search above
                top = row + 1
            else: # target is in this row
                target_row = row
                break
        if target_row == -1:
            return False

        #binary search in this row to find target
        left, right = 0, n - 1
        target_col = -1
        while left <= right:
            col = (left + right) // 2
            if matrix[target_row][col] < target:
                left = col + 1
            elif matrix[target_row][col] > target:
                right = col - 1 
            else:
                return True

        return False              