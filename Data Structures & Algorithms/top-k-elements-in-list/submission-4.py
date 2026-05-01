class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        heap = []
        for num in list(count.keys()):
            heapq.heappush(heap, (count[num], num)) #Has to be count[num] first since it is sorted by this first part of the tuple
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        print(res)
        return res    