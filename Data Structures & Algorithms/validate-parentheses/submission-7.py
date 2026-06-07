class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        valid = {
            '{' : '}',
            '[' : ']',
            '(' : ')'
        }  

        stack = []
        for char in s:
            if char == '{' or char == '(' or char == '[':
                stack.append(char)
            elif char == '}' or char == ')' or char == "]":
                if len(stack) == 0:
                    return False
                stack_char = stack.pop()
                if valid[stack_char] != char:
                    return False
            else:
                return False

        return True if len(stack) == 0 else False                   