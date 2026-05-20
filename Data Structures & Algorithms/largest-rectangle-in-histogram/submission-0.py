class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        for each height in heights
            if the height is less than the previous one:
                pop every height in the stack that is greater than the height and compute the area
            if the height is equal or greater:
                add the height, index into the stack

        '''
        stack = [] # contain [height, index]
        res = -1
        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][0] > height:
                height_s, i_s = stack.pop()
                res = max(res, height_s * (i - i_s))
                start = i_s
            stack.append([height, start])

        while stack:
            height_s, i_s = stack.pop()
            res = max(res, height_s * (len(heights) - i_s))    

        return res    