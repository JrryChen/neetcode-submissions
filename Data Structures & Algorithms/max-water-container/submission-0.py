class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        two end pointers 

        maintain a max area left - right * min(left, right)

        the lower side we move, if even, move the one that next is higher
        '''

        max_area = 0
        left, right = 0, len(heights) - 1

        while left < right:
            max_area = max(max_area, ((right - left) * min(heights[left], heights[right])))
            if heights[left] < heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else:
                left += 1

        return max_area                