
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        heap = []
        for num in list(freq.keys()):
            if len(heap) < k:
                heapq.heappush(heap, (freq[num], num))
            else:
                if freq[num] > heap[0][0]:
                    heapq.heappushpop(heap, (freq[num], num))
        res = []
        for i in range(k):
            res.append(heap[i][1])

        return res    