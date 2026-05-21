class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        calculate arrival times
        if the arrival time is greater than the top of the stack, we pop
        '''
        cars = defaultdict(int)
        for i in range(len(position)):
            cars[position[i]] = speed[i]

        stack = []
        for car in list(sorted(cars.keys(), reverse=True)):
            arrival_t = (target - car) / cars[car]
            stack.append(arrival_t)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)            