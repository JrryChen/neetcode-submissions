class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        ans = False
        for n in freq.keys():
            if freq[n] > 1:
                return True
        return ans        