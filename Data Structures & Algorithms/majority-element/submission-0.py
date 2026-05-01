class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        major = len(nums) / 2
        for num in nums:
            freq[num] += 1
            if freq[num] > major:
                return num