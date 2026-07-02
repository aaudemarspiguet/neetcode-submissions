class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # push operands to stack
        # if run into an operator (+, -, *, /)
        # retrieve last two operands and pop them from the stack (should be empty)
        # combine them using the operator and push to stack
        # continue loop for all elements of the List

        stack: list[int] = []
        operands = {"+", "-", "*", "/"}

        for t in tokens:
            if t not in operands:
                stack.append(int(t))
                continue

            # hit an operator, so first extract operands then determine new value pushed to stack
            y = int(stack[-1]) 
            del stack[-1]

            x = int(stack[-1])
            del stack[-1] # should be empty after this

            if t == "+":
                stack.append(x + y)
            elif t == "-":
                stack.append(x - y)
            elif t == "*":
                stack.append(x * y)
            else:
                stack.append(int(x / y))

        # finally there should be one element in the stack, should be answer
        return stack[-1]
            