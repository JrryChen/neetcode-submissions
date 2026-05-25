import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        group = []
        for n in nums:
            group.append(n)
            j = len(group) - 2
            while j >= 0 and group[j] < group[j + 1]:
                group[j], group[j + 1] = group[j + 1], group[j]
                j -= 1
            while len(group) > k:
                group.pop()

        return group[-1]    