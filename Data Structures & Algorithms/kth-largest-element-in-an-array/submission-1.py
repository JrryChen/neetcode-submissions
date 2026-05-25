import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        group = []
        for n in nums:
            heapq.heappush(group, n)
            if len(group) > k:
                heapq.heappop(group)

        return heapq.heappop(group)   