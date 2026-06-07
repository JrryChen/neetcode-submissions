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
            best_right = -1
            max_h = -1

            while right < len(height):
                if height[right] >= height[left]:
                    best_right = right
                    break
                if height[right] > max_h:
                    max_h = height[right]
                    best_right = right
                right += 1
            
            if best_right != -1:
                h = min(height[left], height[best_right])
                res += (best_right - left - 1) * h - sum(min(h, x) for x in height[left + 1:best_right])
                left = best_right
            else:

                left += 1

        return res