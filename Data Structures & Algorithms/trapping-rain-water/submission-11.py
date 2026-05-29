class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n
        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], height[i-1])
            rightMax[n - 1 - i] = max(rightMax[n-1-i+1], height[n-1-i+1])
        print(leftMax)
        print(rightMax)    
        res = 0
        for i in range(n):
            add = (min(leftMax[i], rightMax[i]) - height[i])
            if add >= 0:
                res += add
            else:
                res += 0    

        return res    