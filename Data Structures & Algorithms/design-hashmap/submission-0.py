class MyHashMap:

    def __init__(self):
        self.mem = [-1] * 10**4
        

    def put(self, key: int, value: int) -> None:
        self.mem[key % 10**4] = value
        return

    def get(self, key: int) -> int:
        return self.mem[key % 10**4]

    def remove(self, key: int) -> None:
        self.mem[key%10**4] = -1
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)