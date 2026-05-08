class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        make nums into a set and iterate through the set to find continuous sequence
        '''
        numsSet = set(nums)
        longest = 0

        for n in numsSet:
            if (n-1) not in numsSet:
                length = 1
                while (n + length) in numsSet:
                    length += 1
                longest = max(longest, length) 

        return longest           