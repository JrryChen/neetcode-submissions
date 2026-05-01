class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        if k = max of piles, then the time would be len(piles)
        min time is len of piles so if its greater than h, then its impossible
        the time it takes to eat a pile of bananas is piles[i] // k + 1
        possible k is 1 to max(piles)
        iterate through to find the min k to eat all banans in h hours (binary search)
        '''
        left, right = 1, max(piles)
        res = max(piles)
        while left <= right:
            k = (left + right) // 2
            total = 0
            for pile in piles:
                total += math.ceil(float(pile) / k)   
            if total <= h: # we want to try to find a smaller k so search on the left side
                res = k
                right = k - 1
            else: # we failed ot eat all the banans so we try to find a bigger k
                left = k + 1

        return res        




        