class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = defaultdict(int) # position : speed
        for i in range(len(position)):
            cars[position[i]] = speed[i]

        stack = [] # stack of arrival times
        for pos in list(sorted(cars.keys(), reverse=True)): 
            stack.append((target-pos) / cars[pos])
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop() 
        return len(stack)                         