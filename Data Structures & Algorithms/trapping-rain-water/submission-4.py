class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        start at first non-zero height = left
        keep goign right until we find a height >= height[left]
        res = right - left * min(height[left], height[right]) - sum(heights we skipped)
        left = right
        if right >= len(heights):
            return
        '''

        left = 0
        while left < len(height) and height[left] == 0:
            left += 1

        res = 0

        while left < len(height):
            right = left + 1

            while right < len(height) and height[right] < height[left]:
                right += 1
            
            if right < len(height):
                res += (right - left - 1) * height[left] - sum(height[left + 1:right])
                left = right
            else:
                # If no wall >= left is found, restart from the end moving backwards to left
                curr_end = len(height) - 1
                while curr_end > left:
                    prev = curr_end - 1
                    while prev >= left and height[prev] < height[curr_end]:
                        prev -= 1
                    if prev >= left:
                        res += (curr_end - prev - 1) * height[curr_end] - sum(height[prev + 1:curr_end])
                    curr_end = prev
                break

        return res