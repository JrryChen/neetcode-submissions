class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                second, first = int(stack.pop()), int(stack.pop())
                stack.append(first + second)
            elif token == '-':
                second, first = int(stack.pop()), int(stack.pop())
                stack.append(first - second)  
            elif token == '*':
                second, first = int(stack.pop()), int(stack.pop())
                stack.append(first * second) 
            elif token == '/':
                second, first = int(stack.pop()), int(stack.pop())
                stack.append(first / second)    
            else:
                stack.append(token)
        return int(stack.pop())               