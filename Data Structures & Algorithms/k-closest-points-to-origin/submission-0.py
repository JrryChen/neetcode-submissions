class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = [] # list of points and ditance
        for x, y in points:
            distance = math.sqrt(x ** 2 + y ** 2)
            hp.append([distance, x, y])
        heapq.heapify(hp)
        res = []
        while k > 0:
              dist, x, y = heapq.heappop(hp)
              res.append([x, y])
              k -= 1
        return res      