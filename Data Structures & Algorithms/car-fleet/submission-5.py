class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = defaultdict(int) # position : speed
        for i in range(len(position)):
            cars[position[i]] = speed[i]

        stack = [] # stack of arrival times
        for pos in list(sorted(cars.keys(), reverse=True)): 
            if len(stack) == 0:
                stack.append((target - pos) / cars[pos])
            else:
                arrival_t = (target - pos) / cars[pos]
                if arrival_t > stack[-1]:
                    stack.append(arrival_t)   
        return len(stack)                         