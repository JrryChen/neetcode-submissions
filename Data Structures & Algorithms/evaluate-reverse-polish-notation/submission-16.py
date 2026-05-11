class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+', '-', '*', '/']
        stack = []

        for token in tokens:
            if token in ops:
                second = stack.pop()
                first = stack.pop()
                if token == "+":
                    stack.append(first + second)
                elif token == '-':
                    stack.append(first - second)
                elif token == "*":
                    stack.append(first * second)
                else: 
                    print(second, first)
                    stack.append(int(first / second))
            else:
                stack.append(int(token))
            print(stack)    

        return stack.pop()                            