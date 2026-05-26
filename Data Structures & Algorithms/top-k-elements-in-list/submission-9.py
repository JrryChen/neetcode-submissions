import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq = Counter(nums)

        for n in list(freq.keys()):
            if len(heap) < k:
                heapq.heappush(heap, (freq[n], n))
            else:
                if freq[n] > heap[0][0]:
                    heapq.heappushpop(heap, (freq[n], n)) 

        res = []
        for _ in range(k):
            res.append(heap[_][1])

        return res                