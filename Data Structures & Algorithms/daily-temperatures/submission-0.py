class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # contains (temp, index)
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                index_p, temp_p = stack.pop()
                res[index_p] = i - index_p
            stack.append((i, temp))  

        return res      