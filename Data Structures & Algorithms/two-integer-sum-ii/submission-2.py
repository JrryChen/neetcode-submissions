class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            cumsum = numbers[l] + numbers[r]
            diff = target - cumsum
            if diff < 0:
                r -= 1
            elif diff > 0:
                l += 1
            else:
                return [l + 1, r + 1]        