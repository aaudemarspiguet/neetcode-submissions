class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: list[int] = []
        operands = {"+", "-", "*", "/"}

        for t in tokens:
            if t not in operands:
                stack.append(int(t))
                continue

            y = stack.pop()
            x = stack.pop()
            
            if t == "+":
                    stack.append(x + y)
            elif t == "-":
                    stack.append(x - y)
            elif t == "*":
                    stack.append(x * y)
            else:
                stack.append(int(x / y))

        return stack[-1]