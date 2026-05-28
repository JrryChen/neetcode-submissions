class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        l = r = 0
        while r < len(nums):
            # pop lesser elements
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            # check if we have an old value in there
            if l > q[0]:
                q.popleft()
            # check if we are at window size
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res                                 