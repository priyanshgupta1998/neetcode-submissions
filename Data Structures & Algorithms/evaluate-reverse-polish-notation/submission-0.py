class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                b = stack.pop()
                a = stack.pop()
                # int(a / b) truncates towards zero properly for positive/negative numbers
                stack.append(int(a / b))
            else:
                stack.append(int(token))

        return stack[0]