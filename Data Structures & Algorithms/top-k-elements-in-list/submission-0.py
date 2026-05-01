class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       freq = Counter(nums)
       res = []
       for pair in freq.most_common()[:k]:
        res.append(pair[0])
       return res 