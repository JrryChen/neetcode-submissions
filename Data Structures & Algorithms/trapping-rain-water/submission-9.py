class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        left = 0
        right = len(height) - 1

        maintain a leftMax and rightMax -> max height encountered by the left or right pointer
        any time we reach a new max, update max, if not, add the gap of max - height

        always move the pointer that is smaller, so it basically always calculated the rain water volume with the min height between right and left
        '''

        left, right = 0, len(height) - 1
        leftMax = height[left]
        rightMax = height[right]
        res = 0

        while left < right:
            if height[left] < height[right]:
                left += 1
                leftMax = max(leftMax, height[left])
                res += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                res += rightMax - height[right]

        return res            