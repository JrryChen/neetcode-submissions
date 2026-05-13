class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            k = (left + right) // 2
            t = 0
            for p in piles:
                t += math.ceil(p / k)
            if t <= h:
                res = k
                right = k - 1
            else:
                left = k + 1

        return res                