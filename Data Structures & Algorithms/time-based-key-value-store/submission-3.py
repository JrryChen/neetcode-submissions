class TimeMap:

    def __init__(self):
        self.dictionary = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dictionary:
            self.dictionary[key] = []
        self.dictionary[key].append([value, timestamp])    

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dictionary:
            return ''
        res = ''
        values = self.dictionary[key]
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l += 1
            else:
                r -= 1    

        return res    
