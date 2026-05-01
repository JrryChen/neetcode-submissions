class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.values = [0] * capacity

    def get(self, i: int) -> int:
        return self.values[i]

    def set(self, i: int, n: int) -> None:
        self.values[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()

        self.values[self.length] = n
        self.length += 1    

    def popback(self) -> int:
        if self.length > 0:
           self.length -= 1
        return self.values[self.length]    
        

    def resize(self) -> None:
        self.capacity *= 2
        self.values.extend([0] * self.capacity)

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity