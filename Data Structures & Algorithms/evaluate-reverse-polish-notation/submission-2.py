# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         stack = []
#         for token in tokens:
#             if token == "+":
#                 second = stack.pop()
#                 first = stack.pop()
#                 stack.append(first + second)
#             elif token == "-":
#                 second = stack.pop()
#                 first = stack.pop()
#                 stack.append(first - second) 
#             elif token == "*":
#                 second = stack.pop()
#                 first = stack.pop()
#                 stack.append(first * second)
#             elif token == '/':
#                 second = stack.pop()
#                 first = stack.pop()
#                 stack.append(first // second)
#             else:
#                 stack.append(int(token))
#         return stack.pop()           
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]