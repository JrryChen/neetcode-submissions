class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = [-1] * capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.data[i]

    def set(self, i: int, n: int) -> None:
        if self.data[i] == -1:
            self.size += 1
        self.data[i] = n    

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.data[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        res = self.data[self.size]
        self.data[self.size] = -1
        return res

    def resize(self) -> None:
        self.data += ([-1] * self.capacity)
        self.capacity *= 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity