from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        if len(tokens) == 1:
            return int(tokens[-1])


        for token in tokens:
            stack.append(token)

            curr = stack[-1]

            if not (token == '+' or token == '-' or token == '*' or token == '/'):
                continue

            operator = stack.pop()
            operand2 = int(stack.pop())
            operand1 = int(stack.pop())

            if operator == '+':
                operand1 = operand1 + operand2
            elif operator == '-':
                operand1 = operand1 - operand2
            elif operator == '*':
                operand1 = operand1 * operand2
            elif operator == '/':
                operand1 = operand1 / operand2
            stack.append(int(operand1))

        return stack[-1]
                