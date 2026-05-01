class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        table = {'(' : ')', '{' : '}', '[':']'}
        q = deque()

        for char in s:
            if char in table.keys():
                q.append(char)
            else:
                if not q:
                    return False
                if table[q.pop()] != char:
                    return False
        if q:
            return False 
                       
        return True            