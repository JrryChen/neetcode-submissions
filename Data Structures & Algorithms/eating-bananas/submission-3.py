class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        binary search from 1 to k and find the min that works
        '''
        left, right = 1, max(piles)
        while left <= right:
            mid = left + (right - left) // 2
            time = 0
            for p in piles:
                time += math.ceil(p / mid)
            if time > h:
                left = mid + 1
            else:
                right = mid - 1
        return left                