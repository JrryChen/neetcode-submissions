class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        longest = 1
        seen = set()

        for num in nums:
            length = 1
            looking = num + 1
            while looking not in seen:
                if looking in nums:
                    length += 1
                    longest = max(longest, length)
                    looking += 1
                else:
                    break

        return longest                

                
